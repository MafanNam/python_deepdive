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

# import sys
# import datetime
# from fractions import Fraction
# from functools import reduce

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


# class Cities:
#     def __init__(self):
#         self._cities = ['angl', 'ball']
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self._cities):
#             raise StopIteration
#         else:
#             item = self._cities[self._index]
#             self._index += 1
#             return item
#
#
# c = Cities()
# for i in c:
#     print(i)
#
#
# class Cities2:
#     def __init__(self):
#         self._cities = ['angl', 'ball']
#
#     def __len__(self):
#         return len(self._cities)
#
#
# c = Cities2()
# for i in c:
#     print(i)


# s = 'sksks sksks'
#
# s_iter = iter(s)
# print(next(s_iter))

#
# _SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
# _RANKS = tuple(range(2, 11)) + tuple('JQKA')
#
# from collections import namedtuple
#
# Card = namedtuple('Card', 'rank suit')
#
# class CardDeck:
#     def __init__(self):
#         self.length = len(_SUITS) * len(_RANKS)
#
#     def __len__(self):
#         return self.length
#
#     def __iter__(self):
#         return self.CardDeckIterator(self.length)
#
#     def __reversed__(self):
#         return self.CardDeckIterator(self.length, reverse=True)
#
#     class CardDeckIterator:
#         def __init__(self, length, reverse=False):
#             self.length = length
#             self.reverse = reverse
#             self.i = 0
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.i >= self.length:
#                 raise StopIteration
#             else:
#                 if self.reverse:
#                     index = self.length - 1 - self.i
#                 else:
#                     index = self.i
#                 suit = _SUITS[index // len(_RANKS)]
#                 rank = _RANKS[index % len(_RANKS)]
#                 self.i += 1
#                 return Card(rank, suit)
#
#
# deck  = CardDeck()
#
# for card in deck:
#     print(card)

# print(list(CardDeck()))

# deck_rev = reversed(deck)
#
# for i in deck_rev:
#     print(i)


# def seq_gen(n):
#     for i in range(n):
#         yield i ** 2
#
# sq = seq_gen(10)
#
# for i in sq:
#     print(i)


# from math import factorial
#
#
# def combo(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))
#
#
# size = 3
#
# pascal = ([combo(n, k) for k in range(n+1)] for n in range(size + 1))
#
# print(list(pascal))


# def matrix(n):
#     gen = ((i * j for j in range(1, n+1)) for i in range(1, n+1))
#     return gen
#
#
# def matrix_iter(n):
#     for row in matrix(n):
#         yield from row
#
#
# for i in matrix_iter(3):
#     print(i)


# l = [1, 2, 3, 4]
#
# print(reduce(lambda x, y: x+y, l))

# s = '1 2 3 4 5 6 7'
# s_map = map(int, s.split(' '))
# print(list(s_map))

# for i in range(5):
#     for j in range(5):
#         print(i, j)
#
# l = [(i, j) for i in range(5) for j in range(5)]
# print(l)
#
# try:
#     f = open('Applications/data/personal_info.csv')
# except:
#     pass
# finally:
#     f.close()
#
#
# with open('Applications/data/personal_info.csv') as f:
#     print(f.read())


# def test():
#     with open('Applications/data/personal_info.csv', 'w') as file:
#         print('inside with: file close', file.closed)
#         return file
#         print('here - will never run')
#
# file = test()

#
# class SubItem:
#     def __init__(self, title, prefix='- ', indent=3):
#         self._title = title
#         self._prefix = prefix
#         self._indent = indent
#         self._current_indent = 0
#         print(title)
#
#     def __enter__(self):
#         self._current_indent += self._indent
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._current_indent -= self._indent
#         return False
#
#     def print(self, arg):
#         s = ' ' * self._current_indent + self._prefix + str(arg)
#         print(s)
#
# lm = SubItem('Main')
# with lm:
#     lm.print('P_1')
#
#     with lm:
#         lm.print('P_2')
#
#
# with lm:
#     lm.print('P_1')
#
#     with lm:
#         lm.print('P_2')
#
#         with lm:
#             lm.print('P_3')
#             lm.print('P_3_1')


# from time import perf_counter, sleep
# # from contextlib import contextmanager
# #
# # @contextmanager
# # def timer():
# #     stars = dict()
# #     start = perf_counter()
# #     stars['start'] = start
# #     try:
# #         yield stars
# #     finally:
# #         end = perf_counter()
# #         stars['end'] = end
# #         stars['elapsed'] = end - start
# #
# # with timer() as t:
# #     sleep(2)
# #
# # print(t)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'c': 30, 'd': 40}
#
# print(d1 | d2)
# print(d2 | d1)

# John = 'John'
# Eric = 'Eric'
# Michael = 'Michael'
# Graham = 'Graham'
#
# persons = [('john', John),
#            ('eric', Eric),
#            ('michael', Michael),
#            ('graham', Graham), ]
#
#
# def search_person(search):
#     for person in persons:
#         if search == person[0]:
#             return person[1]
#     return 'Nothing'
#
#
# search = input('Search person: ')
# print(search_person(search))
#
#
#
# def generate_difference_table(x_values, y_values):
#     n = len(x_values)
#     difference_table = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         difference_table[i][0] = y_values[i]
#
#     for j in range(1, n):
#         for i in range(n - j):
#             difference_table[i][j] = difference_table[i + 1][j - 1] - difference_table[i][j - 1]
#
#     return difference_table
#
# h = 0.5
#
# def calculate_derivative_1():
#     q = 0.76
#     derivative_1 = (1 / h) * (-0.42+( (2 * q - 1) / 2) * (0.01) +( (3 * q ** 2 - 6 * q + 2) / 6) * 0.06 + ((
#             2 * q ** 3 - 9 * q ** 2 + 11 * q - 3) / 12) * 0.015)
#     return derivative_1
#
# def calculate_second_derivative_1():
#     q = 0.76
#     second_derivative_1 = (1 / (h**2)) * (0.01 + (q - 1) * 0.06 + ((6 * (q ** 2) - 18 * q + 11) / 12) * 0.0015)
#     return second_derivative_1
#
# def calculate_derivative_2():
#     q = 0.76
#     derivative_2 = (1 / h) * (-0.195 +((2 * q - 1) / 2) * (0.235) +( (3 * q ** 2 - 6 * q + 2) / 6) * 0.105 + ((
#             2 * q ** 3 - 9 * q ** 2 + 11 * q - 3) / 12) * (0.014))
#     return derivative_2
#
# def calculate_second_derivative_2():
#     q = 0.76
#     second_derivative_2 = (1 / (h ** 2)) * (0.235 + (q - 1) * 0.105 + ((6 * (q ** 2) - 18 * q + 11) / 12) * (0.014))
#     return second_derivative_2
#
# derivative_1 = calculate_derivative_1()
# print(f"Похідна в точці 2.88 = {derivative_1:.3f}")
#
# second_derivative_1 = calculate_second_derivative_1()
# print(f"Друга похідна в точці 2.88 = {second_derivative_1:.3f}")
#
# derivative_2 = calculate_derivative_2()
# print(f"Похідна в точці 4.38 = {derivative_2:.3f}")
#
# second_derivative_2 = calculate_second_derivative_2()
# print(f"Друга похідна в точці 4.38 = {second_derivative_2:.3f}")

# d = {i: i**2 for i in range(1, 6)}
# print(d)
#
# print(list(d.keys()))
# print(d.items())
#
# import random
#
# a = [i for i in range(10)]
# random.shuffle(a)
#
# print(a)
# print(set(a))

# def polynomial_value(x):
#     return 0.374 * x**5 + 0.583 * x**4 - 1.072 * x**3 + 1.548 * x**2 - 2.436 * x - 0.367
#
# x_values = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
# h = 0.25
#
# table = []
#
# for x in x_values:
#     table.append((x, polynomial_value(x)))
#
# for entry in table:
#     print(f"x = {entry[0]}, P(x) = {entry[1]}")


# def f(**kwargs):
#     print(kwargs)
#
# d = {'1': 1, '2': 2}
# print(f(**d))

# a = 10
# b = 10
#
# print(a is b)
#
# a = (10, 10)
# b = (10, 10)
#
# print(a is b)
#
# a = [10, 10]
# b = [10, 10]
#
# print(a is b)
# print(True or True)


# d = dict(zip('abc', range(1, 4)))
#
# item = list(d.items())
#
# for k, v in item:
#     print(k, v)
#     del d['c']

# import json
# from datetime import datetime
#
# d = {'time': '111122', 'a': 111, 'hahha': 'sksksksk'}
#
# print(json.dumps(d, indent=10))
# from collections import defaultdict
#
# d = defaultdict(lambda : 1)
#
# print(d['a'])
# print(d)



# from collections import Counter
#
# counter = Counter()
#
# sentence = 'kdsfksdfk ksdkfdk ferkfr kfke'
#
# for c in sentence:
#     counter[c] += 1
#
# print(counter)

# from collections import ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# d = ChainMap(d1, d2, d3)
#
# print(d, id(d))
# d4 = {'d': 2}
# dd = d.new_child(d4)
# print(dd, id(dd))
# for k, v in d.items():
#     print(k, v)
#
# d = ChainMap(d1, d2, d3)
#
# for k, v in d.items():
#     print(k, v)

# class MyClass:
#     language = 'Python'
#
# d = MyClass
#
# print(d.language)

# def solution(nums):
#     if nums:
#         l = []
#         n = len(nums)
#         for _ in range(n):
#             min_v = min(nums)
#             l.append(min_v)
#             del nums[nums.index(min_v)]
#         return l
#     return []
#
# print(solution([1,2,3,10,5]))


# class My:
#     def f(obj):
#         return 'hello'
#
#
# my = My()
# # print(my.f())
#
# print(my.f, hex(id(my)))


# class Class:
#     def __init__(self):
#         self.__a = 10
#
# cl = Class()
# print(cl.__a)
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#
# p = Person('Jons')
#
# print(p.name)
# p.name = 0
# print(p.name)

