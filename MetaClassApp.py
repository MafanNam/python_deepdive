
# class Point2D:
#     _fields = ['x', 'y']
#
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# class Point3D:
#     _fields = ['x', 'y', 'z']
#
#     def __init__(self, x, y, z):
#         self._x = x
#         self._y = y
#         self._z = z


class SlottedStruct(type):
    def __new__(mcls, name, bases, class_dict):
        cls_obj = super().__new__(mcls, name, bases, class_dict)

        # __slots__ = ()
        setattr(cls_obj, '__slots__', [f"_{field}" for field in cls_obj._fields])

        # read-only prop
        for field in cls_obj._fields:
            slot = f"_{field}"
            setattr(cls_obj, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

        # __eq__
        def eq(self, other):
            if isinstance(other, cls_obj):
                self_fields = [getattr(self, field) for field in cls_obj._fields]
                other_fields = [getattr(other, field) for field in cls_obj._fields]
                return self_fields == other_fields
        setattr(cls_obj, '__eq__', eq)

        # __hash__
        def hash_(self):
            field_values = (getattr(self, field) for field in cls_obj._fields)
            return hash(tuple(field_values))
        setattr(cls_obj, '__hash__', hash_)

        # __str__
        def str_(self):
            field_values = (getattr(self, field) for field in cls_obj._fields)
            field_values_joined = ', '.join(map(str, field_values))
            return f"{cls_obj.__name__}({field_values_joined})"
        setattr(cls_obj, '__str__', str_)

        # __repr__
        def repr_(self):
            field_values = (getattr(self, field) for field in self._fields)
            field_key_values = (f"{key}={value}" for key, value in zip(self._fields, field_values))
            field_key_values_str = ', '.join(field_key_values)
            return f"{cls_obj.__name__}({field_key_values_str})"
        setattr(cls_obj, '__repr__', repr_)

        return cls_obj


# class Person(metaclass=SlottedStruct):
#     _fields = ['name', 'age']
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
# print(vars(Person))
# p = Person('alex', 10)
# print(p.name)

# class Person(metaclass=SlottedStruct):
#     _fields = ['name']
#
#     def __init__(self, name):
#         self._name = name
#
# print(type(Person))
# # print(vars(Person))
# p1 = Person('alex')
# p2 = Person('alex')
# print(p1 == p2)
# print(p1)
# print(p2.__repr__())


class Point2D(metaclass=SlottedStruct):
    _fields = ['x', 'y']

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Point3D(metaclass=SlottedStruct):
    _fields = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z













