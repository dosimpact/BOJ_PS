import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


T = int(input())

for _ in range(T):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(2)]  # 스티커 [위,아래][열r]
    d: List[List[int]] = [[0 for _ in range(3)] for _ in range(N)]  # N-1 까지 구함
    d[0][1] = P[0][0]
    d[0][2] = P[1][0]
    for r in range(1, N):
        d[r][0] = max(d[r-1][0], d[r-1][1], d[r-1][2])
        d[r][1] = max(d[r-1][0], d[r-1][2]) + P[0][r]
        d[r][2] = max(d[r-1][0], d[r-1][1]) + P[1][r]
    print(max(d[N-1]))
