import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


X = int(input())

d = [0 for _ in range(10**6+1)]
d[2] = 1
d[3] = 1
for i in range(4, 10**6+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)


print(d[X])
