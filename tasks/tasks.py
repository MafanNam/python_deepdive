# from random import random
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# a = sorted(l, key=lambda x: random())
# print(a)

# ----------------------goal_1-------------------------------
# def sort_dict_by_value(d):
#     t = sorted(d.items(), key=lambda x: x[-1])
#     return dict(t)
#
# composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

# print(sort_dict_by_value(composers))


# ----------------------goal_2-------------------------------

# def set_dict_sort_contain(d1, d2):
#     d1k = d1.keys()
#     d2k = d2.keys()
#     dk = d1k & d2k
#     return dict((k, (d1[k], d2[k])) for k in dk)
#
# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

# print(set_dict_sort_contain(d1, d2))

# ----------------------goal_3-------------------------------
#
#
# def zip_dict(*dicts):
#     unsorted = {}
#     for d in dicts:
#         for k, v in d.items():
#             unsorted[k] = unsorted.get(k, 0) + v
#
#     return dict(sorted(unsorted.items(), key=lambda x: x[-1], reverse=True))
#
#
#
#
# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
#
# print(zip_dict(d1, d2, d3))

# ----------------------goal_4-------------------------------

# def identity(node1, node2, node3):
#     union = node1.keys() | node2.keys() | node3.keys()
#     intersection = node1.keys() & node2.keys() & node3.keys()
#     relevant = union - intersection
#     print(union)
#     print(intersection)
#     print(relevant)
#     result = {
#         key: (node1.get(key, 0), node2.get(key, 0), node3.get(key, 0)) for key in relevant
#     }
#     return result
#
#
# n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
# n2 = {'employees': 250, 'users': 23, 'user': 230}
# n3 = {'employees': 120, 'users': 4, 'login': 1000}
#
# print(identity(n1, n2, n3))


# ----------------------goal_1-------------------------------


# def zip_dict(*dicts):
#     unsorted = {}
#     for d in dicts:
#         for k, v in d.items():
#             unsorted[k] = unsorted.get(k, 0) + v
#
#     return dict(sorted(unsorted.items(), key=lambda x: x[-1], reverse=True))
#
# from collections import Counter
#
#
#
# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
#
# d = Counter()
#
# d.update(d1)
# d.update(d2)
# d.update(d3)
# print(d)


# ----------------------goal_2-------------------------------
#
# eye_colors = ('amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red', 'violet')
#
#
# class Person:
#     def __init__(self, eye_color):
#         self.eye_color = eye_color
#
#
# from random import seed, choices
# from collections import Counter
#
# seed(0)
#
# persons = [Person(color) for color in choices(eye_colors[2:], k=50)]
#
# # print(persons)
#
# def count_persons(persons):
#     d = Counter()
#     for person in persons:
#         d[person.eye_color] += 1
#
#     return d
#
#
# print(count_persons(persons))



# ----------------------goal_3-------------------------------

from collections import ChainMap
import json
from pprint import pprint

def loads_setting(env):
    with open(f"{env}.json") as f:
        settings = json.load(f)
    return settings

# common = loads_setting('common')
# dev = loads_setting('dev')
# prod = loads_setting('prod')

def settings(env):
    common_settings = loads_setting('common')
    env_settings = loads_setting(env)
    return ChainMap(env_settings, common_settings)

dev = settings('dev')

for k, v in dev.items():
    print(k, ':', v)







