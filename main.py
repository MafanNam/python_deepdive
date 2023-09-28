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

# str
# from time import perf_counter
# from collections import namedtuple
#
# Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')
#
#
# def compare_timings(timing1, timing2):
#     rel_diff = (timing2 - timing1) / timing1 * 100
#
#     timings = Timings(round(timing1, 1), round(timing2, 1),
#                       round(timing2 - timing1, 1), round(rel_diff, 2))
#
#     return timings
#
#
# test_repeats = 10_000_000

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


# s = '(log) I can more then you can do'

# print(s.removesuffix())

# from random import randint

# print(randint(2, 100))

# import sys
#
# print(sys.argv[1:])
# print('fffffffff')

# print('' + '' + '' + 'f')
# t = int(input('t= '))
#
# match t:
#     case 1:
#         print('hi 1')
#     case 2:
#         print('hi 2')
#
#
# def switcher(fn):
#     registry = dict()
#     registry['default'] = fn
#
#     def register(case):
#         def inner(fn):
#             registry[case] = fn
#             return fn
#
#         return inner
#
#     def decorator(case):
#         fn = registry.get(case, registry['default'])
#
#         return fn
#
#     decorator.register = register
#     return decorator
#
#
# @switcher
# def dow():
#     return 'Invalid day in week'
#
# @dow.register(1)
# def dow_1():
#     return 'Monday'
#
# dow.register(2)(lambda: 'Tuesday')
# dow.register(3)(lambda: 'Wednesday')
# dow.register(4)(lambda: 'Thursday')
#
#
# print(dow(2)())

# print(None * 3)
# print(str(None) * 3)

# from timeit import timeit
#
# print(timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10_000_000))
# print(timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10_000_000))

# a = slice(2, 6, 1)
#
# l = 'python'
#
# print(l[a])

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(l.__getitem__(-1))
# print(l[-1])


# from functools import lru_cache
#
#
# @lru_cache(2 ** 10)
# def fib(n):
#     if n < 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(10))
# print(fib(100))
# print(fib(500))
# print(fib(700))
# print(fib(900))

# print('-' * 20, 'List', '-' * 20)
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(hex(id(l1)))
# print(hex(id(l2)))
#
# l1 += l2
#
# print(hex(id(l1)))
#
# print('-' * 20, 'Tuple', '-' * 20)
#
# l1 = (1, 2, 3)
# l2 = (4, 5, 6)
#
# print(hex(id(l1)))
# print(hex(id(l2)))
#
# l1 += l2
#
# print(hex(id(l1)))


# sq = [i**2 for i in range(100)]
# print(sq)
# # print(i)
#
# sq2 = []
# for i in range(100):
#     sq2.append(i**2)
#
# print(sq2)
# print(i)
#
# from math import factorial
#
# def combo(n, k):
#     return factorial(n) // (factorial(k) * factorial(n-k))
#
# size = 10
#
# pascal = [[combo(n, k) for k in range(n+1)] for n in range(size+1)]
#
# print(*pascal, sep='\n')


# l1 = ['a', 'b', 'c']
# l2 = ['x', 'y', 'x']
#
# res = [i+j for i in l1 for j in l2]
# print(res)

# l1 = ['a', 'b', 'c']
# l2 = ['x', 'b', 'c']
#
# res = [i+j for i in l1 for j in l2 if i != j]
# print(res)




