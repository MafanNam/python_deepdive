import numbers


# class IntegerField:
#     def __init__(self, min_value=None, max_value=None):
#         self._min_value = min_value
#         self._max_value = max_value
#
#     def __set_name__(self, owner, property_name):
#         self.property_name = property_name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.property_name, None)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, numbers.Integral):
#             raise ValueError(f"value {value} must be an integer")
#         if self._min_value is not None and self._min_value > value:
#             raise ValueError(f"value must be greatest")
#         if self._max_value is not None and self._max_value < value:
#             raise ValueError(f"value must be latest")
#         instance.__dict__[self.property_name] = value
#
#
# class CharField(IntegerField):
#     def __init__(self, min_value=1, max_value=None):
#         super().__init__(min_value, max_value)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"value {value} must be an string")
#         if self._min_value is not None and self._min_value > len(value):
#             raise ValueError(f"value must be greatest")
#         if self._max_value is not None and self._max_value < len(value):
#             raise ValueError(f"value must be latest")
#         instance.__dict__[self.property_name] = value


# class Person:
#     name = CharField(max_value=10)
#     age = IntegerField(0, 200)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p = Person('gg', 5)
# # p.age = 0
# print(p.name)
# print(p.age)


class BaseValidator:
    def __init__(self, min_value=None, max_value=None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def validate(self, value):
        self.validate(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.property_name] = value


class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f"value {value} must be an integer")
        if self._min_value is not None and self._min_value > value:
            raise ValueError(f"value must be greatest")
        if self._max_value is not None and self._max_value < value:
            raise ValueError(f"value must be latest")


class CharField(BaseValidator):
    def __init__(self, min_value=None, max_value=None):
        min_value = min_value or 0
        min_value = max(min_value, 0)
        super().__init__(min_value, max_value)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"value {value} must be an string")
        if self._min_value is not None and self._min_value > len(value):
            raise ValueError(f"value must be greatest")
        if self._max_value is not None and self._max_value < len(value):
            raise ValueError(f"value must be latest")


class Person:
    name = CharField(max_value=10)
    age = IntegerField(0, 200)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('gg', 5)
# p.age = 0
print(p.name)
print(p.age)
