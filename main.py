# a = 'hello'
#
# print(list(enumerate(a)))


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self._height = height

    def get__width(self):
        return self.__width


r1 = Rectangle(10, 20)
print(r1.get__width())
print(r1._height)
