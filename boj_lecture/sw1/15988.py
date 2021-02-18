import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

d = [0 for _ in range(0, 10**6+1)]
d[1] = 1
d[2] = d[1]+1
d[3] = d[1]+d[2]+1
DIVIDER = 1000000009

for i in range(4, 10**6+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]
    d[i] = d[i] % DIVIDER


T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])
