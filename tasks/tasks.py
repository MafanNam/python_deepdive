from random import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = sorted(l, key=lambda x: random())
print(a)