# a = 'hello'
#
# print(list(enumerate(a)))


# class Rectangle:
#     def __init__(self, width, height):
#         self.__width = width
#         self._height = height
#
#     def get__width(self):
#         return self.__width
#
#
# r1 = Rectangle(10, 20)
# print(r1.get__width())
# print(r1._height)

# a = [1, 2]
# print(id(a[0]))
#
# b = (1, 2)
# print(id(b[0]))

# a = 'Последние слова, произнесенные Королем Пиратов перед казнью, вдохновили многих: «Мои сокровища? Коли хотите, забирайте. Ищите – я их все оставил там!». Легендарная фраза Золотого Роджера ознаменовала начало Великой Эры Пиратов – тысячи людей в погоне за своими мечтами отправились на Гранд Лайн, самое опасное место в мире, желая стать обладателями мифических сокровищ. '
# b = 'Последние слова, произнесенные Королем Пиратов перед казнью, вдохновили многих: «Мои сокровища? Коли хотите, забирайте. Ищите – я их все оставил там!». Легендарная фраза Золотого Роджера ознаменовала начало Великой Эры Пиратов – тысячи людей в погоне за своими мечтами отправились на Гранд Лайн, самое опасное место в мире, желая стать обладателями мифических сокровищ. '

# print(a is b)
# print(id(a), id(b))
# print(a == b)

import sys
import datetime
from fractions import Fraction


# print(sys.getsizeof(443773373737**444))

# def calc(a):
#     for i in range(100000000000000000):
#         a * 2
#
#
# start = datetime.datetime.now()
# calc(2 * 1000000000000000000000000)
# end = datetime.datetime.now()
#
# print(end - start)

# print(type(10/3))
#
# a = 0b101
#
# print(a)
#
# print(round(1.333, 2))
# print(round(1.333, 1))
# print(round(14.333, -1))

# print(format(0.1, '.64f'))

# print(True+True)

# print(float(True))

# print(bool(''))
# print(bool(1 + 0j))
# print(bool(0 + 0j))
#
# print(help(list))

# print(bool(x))

# a = (,)

# print(len(None))


# a = None
#
# if a is not None and len(a) > 0:
#     print('good')
# else:
#     print('bad')


# print((1, 2) is (1, 2))
#
# print(Fraction(2, 3))

# a = (1, 2, 3, 4, 5)
#
# c, *v = a
#
# print(c, v)

# my_func = lambda x: x ** 2
#
# print(my_func(4))
# print(my_func.__annotations__)

# TODO: test func
# and some notes
# def func():
#     pass


# a = {1, 5, 33, 0, 1, 4, 5, 7, 4, 222}
#
# print(max(a))

# a = 1
#
# def f():
#     a = 'fff'
#     print(a)
#
# f()
# print(a)

# a = 1
#
# def f():
#     print(a)
#     a = 3

# a = 3
#
# f = lambda n: (a**n, a)
#
# print(f(4))
#
# print(f.__globals__)

# def outher():
#     # global x
#     x = 'hello'
#
#     def innner():
#         global x
#         x = 'pytho'
#
#     innner()
#
#     print(x)
#
# print(outher())
#
# x = 'fdsf'
#
# def f():
#     x = 0
#     def g():
#         nonlocal x
#         x = 44
#
#
# f()
# print(x)

# x = 33
#
# def f():
#     nonlocal x
#     x = 3
#
# f()

# def counter(fn):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(count)
#
#         return fn(*args, **kwargs)
#     return inner
#
# @counter
# def add(a, b):
#     return a + b
#
# print(add(3, 5))
# print(add(3, 5))
# print(add(3, 5))
# print(add(3, 5))
# print(add(3, 5))


# def diamond(n):
#     s = []
#     for i in range(1, n + 1, 2):
#         s.append(' ' * (n // 2 - (i-1)) + '*' * i + '\n')
#
#     for j in range(n, 1, 2):
#         s.append(' ' * (n - j - 1) + '*' * j + '\n')
#
#     return ''.join(s)
#
#
# print(diamond(5))


# def title_case(title: str, minor_words='') -> str:
#     title = title.title().split()
#     minor_words = minor_words.lower().split(' ')
#     for i in range(1, len(title)):
#         if title[i].lower() in minor_words:
#             title[i] = title[i].lower()
#     return ' '.join(title)
#
#
# print(title_case('a clash of KINGS', 'a an the of'))
#
#
# def f(s):
#     s = s.title()
#     s = s.replace(' ', '')
#
#     return '#' + s
#
# s = '    fjfjfj   fkfkfk    '
#
# print(f(s))


# def cockroach_speed(s: int):
#     return s.__floor__()























