import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# N = int(input().split())

d = [[0 for _ in range(3)] for _ in range(0, 100001)]

d[1][0] = 1
d[2][1] = 1
d[3][0] = d[3][1] = d[3][2] = 1

DIVER = 1000000009

for i in range(4, 100001):
    # 1을 붙이는 경우
    d[i][0] = d[i-1][1] + d[i-1][2]
    d[i][0] = d[i][0] % DIVER
    # 2를 붙이는 경우
    d[i][1] = d[i-2][0] + d[i-2][2]
    d[i][1] = d[i][1] % DIVER
    # 3을 붙이는 경우
    d[i][2] = d[i-3][0] + d[i-3][1]
    d[i][2] = d[i][2] % DIVER

T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(d[N]) % DIVER)
