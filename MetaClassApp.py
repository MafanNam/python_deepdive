# --------------------app-1-----------------------
#
#
# # class Point2D:
# #     _fields = ['x', 'y']
# #
# #     def __init__(self, x, y):
# #         self._x = x
# #         self._y = y
# #
# #
# # class Point3D:
# #     _fields = ['x', 'y', 'z']
# #
# #     def __init__(self, x, y, z):
# #         self._x = x
# #         self._y = y
# #         self._z = z
#
#
# class SlottedStruct(type):
#     def __new__(mcls, name, bases, class_dict):
#         cls_obj = super().__new__(mcls, name, bases, class_dict)
#
#         # __slots__ = ()
#         setattr(cls_obj, '__slots__', [f"_{field}" for field in cls_obj._fields])
#
#         # read-only prop
#         for field in cls_obj._fields:
#             slot = f"_{field}"
#             setattr(cls_obj, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))
#
#         # __eq__
#         def eq(self, other):
#             if isinstance(other, cls_obj):
#                 self_fields = [getattr(self, field) for field in cls_obj._fields]
#                 other_fields = [getattr(other, field) for field in cls_obj._fields]
#                 return self_fields == other_fields
#         setattr(cls_obj, '__eq__', eq)
#
#         # __hash__
#         def hash_(self):
#             field_values = (getattr(self, field) for field in cls_obj._fields)
#             return hash(tuple(field_values))
#         setattr(cls_obj, '__hash__', hash_)
#
#         # __str__
#         def str_(self):
#             field_values = (getattr(self, field) for field in cls_obj._fields)
#             field_values_joined = ', '.join(map(str, field_values))
#             return f"{cls_obj.__name__}({field_values_joined})"
#         setattr(cls_obj, '__str__', str_)
#
#         # __repr__
#         def repr_(self):
#             field_values = (getattr(self, field) for field in self._fields)
#             field_key_values = (f"{key}={value}" for key, value in zip(self._fields, field_values))
#             field_key_values_str = ', '.join(field_key_values)
#             return f"{cls_obj.__name__}({field_key_values_str})"
#         setattr(cls_obj, '__repr__', repr_)
#
#         return cls_obj
#
#
# # class Person(metaclass=SlottedStruct):
# #     _fields = ['name', 'age']
# #
# #     def __init__(self, name, age):
# #         self._name = name
# #         self._age = age
# #
# # print(vars(Person))
# # p = Person('alex', 10)
# # print(p.name)
#
# # class Person(metaclass=SlottedStruct):
# #     _fields = ['name']
# #
# #     def __init__(self, name):
# #         self._name = name
# #
# # print(type(Person))
# # # print(vars(Person))
# # p1 = Person('alex')
# # p2 = Person('alex')
# # print(p1 == p2)
# # print(p1)
# # print(p2.__repr__())
#
#
# class Point2D(metaclass=SlottedStruct):
#     _fields = ['x', 'y']
#
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# class Point3D(metaclass=SlottedStruct):
#     _fields = ['x', 'y', 'z']
#
#     def __init__(self, x, y, z):
#         self._x = x
#         self._y = y
#         self._z = z


# --------------------app-2-----------------------
#
#
# # class Hundred:
# #     _existing_instance = None
# #
# #     def __new__(cls):
# #         if not cls._existing_instance:
# #             print('creating new instance...')
# #             new_instance = super().__new__(cls)
# #             setattr(new_instance, 'name', 'hundred')
# #             setattr(new_instance, 'value', 100)
# #             cls._existing_instance = new_instance
# #         else:
# #             print('instance exists already, using that one...')
# #         return cls._existing_instance
#
#
# # h1 = Hundred()
# #
# # h2 = Hundred()
# #
# # print(h1 is h2)
#
#
# class Singleton(type):
#     instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         print(f"Request received to create an instance of class: {cls}...")
#         existing_instance = Singleton.instances.get(cls, None)
#         if existing_instance is None:
#             print('Creating instance for the first time...')
#             Singleton.instances[cls] = super().__call__(*args, **kwargs)
#         else:
#             print('Using existing instance...')
#         return Singleton.instances[cls]
#
#
# class Hundred(metaclass=Singleton):
#     value = 100


# --------------------app-3-----------------------
import configparser


with open('prod.ini', 'w') as prod, open('dev.ini', 'w') as dev:
    prod.write('[Database]\n')
    prod.write('db_host=prod.mynetwork.com\n')
    prod.write('db_name=my_database\n')
    prod.write('\n[Server]\n')
    prod.write('port=8080\n')

    dev.write('[Database]\n')
    dev.write('db_host=dev.mynetwork.com\n')
    dev.write('db_name=my_database\n')
    dev.write('\n[Server]\n')
    dev.write('port=3000\n')


class Config:
    def __init__(self, env='dev'):
        print(f"Loading config from {env} file")
        config = configparser.ConfigParser()
        file_name = f"{env}.ini"
        config.read(file_name)
        self.db_host = config['Database']['db_host']
        self.db_name = config['Database']['db_name']
        self.port = config['Server']['port']



