import time


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


def average():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


# a = average()
# print(a(10))
# print(a(20))
# print(a(30))
# print(a(40))

from time import perf_counter


class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


# t1 = Timer()
# time.sleep(4)
# print(t1())


def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

# counter1 = counter()
#
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())


def counter_v2(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        # print(f"{} has been called")
