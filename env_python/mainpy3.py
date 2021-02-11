import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
An = []
for _ in range(N):
    An.append(int(input()))


d = [[0 for _ in range(3)] for i in range(N+1)]  # [n 번째 포도주를][k번 연속 마셨다.]
d[0][1] = An[0]
for i in range(1, N):  # 0...N-1 번째 포도주 처리
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + An[i]
    d[i][2] = d[i-1][1] + An[i]

print(max(d[N-1]))
