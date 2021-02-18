import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
P = [0]+list(map(int, input().split()))
d = [10**7 for _ in range(1001)]
d[0] = 0
d[1] = P[1]

for i in range(2, N+1):  # 2
    for j in range(1, i+1):  # 1,2
        d[i] = min(d[i], d[i-j]+P[j])

print(d[N])
