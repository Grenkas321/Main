from collections import Counter
from timeit import *

def counte(mas):
    return Counter(mas)

def dic(mas):
    d = {}
    for i in mas:
        d[i] = d.get(i, 0) + 1
    return d

mas = input().split()
print(Timer("counte(mas)", globals = globals()).autorange())
print(Timer("dic(mas)", globals = globals()).autorange())
