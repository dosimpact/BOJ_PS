import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

DIVIDER = 10007

d = [0 for _ in range(1001)]
d[1] = 1
d[2] = 3
for i in range(3, 1001):
    d[i] = d[i-1]+d[i-2]*2
    d[i] = d[i] % DIVIDER

N = int(input())
print(d[N])
