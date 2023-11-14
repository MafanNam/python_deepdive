class Int:
    def __set_name__(self, owner, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.prop_name} must be an integer.")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)


class Float:
    def __set_name__(self, owner, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f"{self.prop_name} must be an float.")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)


class List:
    def __set_name__(self, owner, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f"{self.prop_name} must be an list.")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)



class ValidType:
    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, owner, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"{self.prop_name} must be an type {self._type.__name__}.")
        instance.__dict__[self.prop_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.prop_name, None)


class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)

p = Person()

try:
    p.tags = 'df'
except ValueError as ex:
    print(ex)




