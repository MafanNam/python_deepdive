from abc import ABC
from numpy import exp
import math
import random


class Zubec(ABC):
    def get(self, t):
        t, _ = math.modf(t)
        b = self.b1 if t <= self.m else self.b2
        return self.A * exp(-(t - self.m) ** 2 / (b ** 2))


class P(Zubec):
    def __init__(self):
        self.m = 0.4
        self.b1 = 0.02
        self.b2 = 0.02
        self.A = 0.1


class Q(Zubec):
    def __init__(self):
        self.m = 0.47
        self.b1 = 0.01
        self.b2 = 0.0085
        self.A = -0.13


class R(Zubec):
    def __init__(self):
        self.m = 0.5
        self.b1 = 0.0079
        self.b2 = 0.0079
        self.A = 1


class S(Zubec):
    def __init__(self):
        self.m = 0.53
        self.b1 = 0.0085
        self.b2 = 0.01
        self.A = -0.18


class ST(Zubec):
    def __init__(self):
        self.m = 0.61
        self.b1 = 0.028
        self.b2 = 0.028
        self.A = 0.00


class T(Zubec):
    def __init__(self):
        self.m = 0.75
        self.b1 = 0.018
        self.b2 = 0.008
        self.A = 0.2
        self._lambda = 1

    def get_alternation(self, t):
        t, m = math.modf(t)
        _lambda = 1 if int(m) % 2 == 0 else self._lambda
        return _lambda * self.get(t)


class EKG:
    def __init__(self):
        self.zubci = [P(), Q(), R(), S(), ST(), T()]
        self.T = self.zubci[-1]
        self.h = 0.1

    def get(self, t):
        return sum([x.get(t) for x in self.zubci])

    def get_alternation(self, t):
        self.T.b1 = 0.018
        self.T.b2 = 0.018
        return sum([x.get(t) for x in self.zubci[:-1]]) + \
            self.T.get_alternation(t) + \
            random.uniform(-0.05, 0.05) * self.h
