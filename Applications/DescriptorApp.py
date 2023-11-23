# class Int:
#     def __set_name__(self, owner, prop_name):
#         self.prop_name = prop_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise ValueError(f"{self.prop_name} must be an integer.")
#         instance.__dict__[self.prop_name] = value
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.prop_name, None)
#
#
# class Float:
#     def __set_name__(self, owner, prop_name):
#         self.prop_name = prop_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, float):
#             raise ValueError(f"{self.prop_name} must be an float.")
#         instance.__dict__[self.prop_name] = value
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.prop_name, None)
#
#
# class List:
#     def __set_name__(self, owner, prop_name):
#         self.prop_name = prop_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, list):
#             raise ValueError(f"{self.prop_name} must be an list.")
#         instance.__dict__[self.prop_name] = value
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.prop_name, None)
#
#
#
# class ValidType:
#     def __init__(self, type_):
#         self._type = type_
#
#     def __set_name__(self, owner, prop_name):
#         self.prop_name = prop_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self._type):
#             raise ValueError(f"{self.prop_name} must be an type {self._type.__name__}.")
#         instance.__dict__[self.prop_name] = value
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.prop_name, None)
#
#
# class Person:
#     age = ValidType(int)
#     height = ValidType(float)
#     tags = ValidType(list)
#     favorite_foods = ValidType(tuple)
#
# p = Person()
#
# try:
#     p.tags = 'df'
# except ValueError as ex:
#     print(ex)


# ------------------------app2--------------------------------


class Int:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an int.")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be grater than {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)


class Point2D:
    x = Int(min_value=0, max_value=800)
    y = Int(min_value=0, max_value=600)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point2D) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# p = Point2D(-1, 3)

import _collections_abc


class Point2DSequence:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, _collections_abc.Sequence):
            raise ValueError(f"{self.name} must be a sequence type.")
        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(f"{self.name} must be grater than {self.max_value}")

        for index, item in enumerate(value):
            if not isinstance(item, Point2D):
                raise ValueError(f"Item at index {index} is not a Point2D instance.")

        instance.__dict__[self.name] = list(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = []
        return instance.__dict__.get(self.name)


class Polygon:
    vertices = Point2DSequence(min_value=3)

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, pt):
        if not isinstance(pt, Point2D):
            raise ValueError('Can only append Point2D.')
        max_value = type(self).vertices.max_value
        if max_value is not None and len(self.vertices) >= max_value:
            raise ValueError(f"Vertices length is at max ({max_value}).")
        self.vertices.append(pt)

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, item):
        return self.vertices[item]

    def __iadd__(self, other):
        self.append(other)
        return self

    def __contains__(self, item):
        return item in self.vertices


# try:
#     p = Polygon()
# except ValueError as ex:
#     print(ex)


# try:
#     p = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
# except ValueError as ex:
#     print(ex)
# p.append(Point2D(10, 10))
#
# print(p.vertices)

class Triangle(Polygon):
    vertices = Point2DSequence(min_value=3, max_value=3)


class Rectangle(Polygon):
    vertices = Point2DSequence(min_value=4, max_value=4)


p = Polygon(Point2D(0, 0), Point2D(0, 1), Point2D(1, 0))
p += Point2D(20, 20)
print(list(p))
