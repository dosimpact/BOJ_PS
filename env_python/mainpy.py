import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())

# 0 시작 가능
d = [[0 for _ in range(2)] for _ in range(90+1)]

d[1][0] = 0
d[1][1] = 1
d[2][0] = d[1][0] + d[1][1]  # 10 00
d[2][1] = d[1][0]

for i in range(2, N+1):  # 자리수
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

print(sum(d[N]))
