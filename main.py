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


# write the function is_anagram
# def is_anagram(test, original):
#     test = sorted(test.lower())
#     original = sorted(original.lower())
#
#     return [False, True][test==original]


# print(is_anagram("foefet", "toffee"))


# def solution(nums):
#     t = nums[0]
#
#
#
# print(solution([1,2,3,10,5]))


# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Point2D(x={self.x}, y={self.y})"
#
#     def __eq__(self, other):
#         if isinstance(other, Point2D):
#             return self.x == other.x and self.y == other.y
#         else:
#             return False

# x = {'x': 10, 'y': 20, 'z': 30}
#
# print(x)

str
from time import perf_counter
from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')


def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1) / timing1 * 100

    timings = Timings(round(timing1, 1), round(timing2, 1),
                      round(timing2 - timing1, 1), round(rel_diff, 2))

    return timings


test_repeats = 10_000_000

# import math
#
# start = perf_counter()
#
# for _ in range(test_repeats):
#     math.sqrt(2)
#
# end = perf_counter()
# elapsed_fully_qualified = end - start
# print(f"Elapsed: {elapsed_fully_qualified}")

# from math import sqrt
#
# start = perf_counter()
#
# for _ in range(test_repeats):
#     sqrt(2)
#
# end = perf_counter()
# elapsed_direct_qualified = end - start
# print(f"Elapsed: {elapsed_direct_qualified}")

# print(compare_timings(elapsed_fully_qualified, elapsed_direct_qualified))

# if __name__ == '__main__':
#     print(f"start main.py == {__name__}")
#     import __main__



# d = {'f': 333, 'dd': 234}
#
# print(d.items(), d.keys())

# from datetime import datetime
# from math import pi
#
# d = datetime.utcnow()
#
# e = pi
#
# print(f"{d=}, {e=}")
# print(f"{d=:%Y-%m-%d}, {e=:.3f}")
# print(d, e)
#
# print(f"{1 + 2 = }")


s = '(log) I can more then you can do'

print(s.removesuffix())

import math

print("**** Task 1 ****")

def first(x, X):
    return abs(x - X)/x

n1, x1 = 38, 6.16

X1 = math.sqrt(n1)
dx1 = first(x1, X1)
print(f"dx1 = {dx1}")

n2, N2, x2 = 5, 3, 1.667

X2 = n2/N2
dx2 = first(x2, X2)
print(f"dx2 = {dx2}")

answer = 0
print(f"sqrt({n1})  is more accurate" if dx1 < dx2 else f"{n2}/{N2}  is more accurate")
print("")
print("**** Task 2 a) ****")

x, dx, a, i = 0.98351, 0.00042, 0.5, 0

while dx < a/10:
    a /= 10; i += 1

fdx = round(dx + abs(round(x, i) - x), 4)

while fdx > a:
    i -= 1; a *= 10
    tmp = abs(round(x, i))
    fdx = round(dx + abs(round(x, i) - x), 4)

print(f"In rounded number x = {fdx} all numbers are true in the narrow sense ")
print("")
print("**** Task 2 b) ****")

x, sx = 3.7542, 0.32

dx, er, i = x*sx/100, 1, 0
if x > 9: i -= 1
while dx < er: er /= 10; i += 1
er *= 10

ndx = dx + abs(round(x, i) - x)
while ndx < er:
    i -= 1
    ndx = dx + abs(round(x, i) - x)

print(f"In rounded number x* = {round(x, i)} all numbers are true in the broad sense ")
print("")
print("**** Task 3 a) ****")

x = 62.74
x2, i = x, 0

while int(x2) != x:
    i += 1
    x, x2 = x*10, x2*10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10**i
dx = (0.1/(10**i))*5
sx = dx/x
print(f"∆x = {dx}, σx = {sx} ({sx*100}%)")
print("")
print("**** Task 3 b) ****")

x = 0.389
x2, i = x, -1

while int(x2) != x:
    i += 1
    x, x2 = x*10, x2*10
    x, x2 = round(x, 7), round(x2, 7)

x /= 10**(i+1)
dx = 0.1/(10**i)
sx = dx/x
print(f"∆x = {dx}, σx = {sx} ({sx*100}%)")

