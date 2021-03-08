import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

d = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]


d[0][0][graph[0][0]] = 1

for i in range(0, N):
    for j in range(0, N):
        for k in range(3):  # 유지 | 먹는 경우 |
            if i - 1 >= 0 and d[i][j][k] < d[i - 1][j][k]:
                d[i][j][k] = d[i - 1][j][k]
            if j - 1 >= 0 and d[i][j][k] < d[i][j - 1][k]:
                d[i][j][k] = d[i][j - 1][k]
            if (
                graph[i][j] == k
                and i - 1 >= 0
                and d[i][j][k] < d[i - 1][j][(k - 1) % 3] + 1
            ):
                d[i][j][k] = d[i - 1][j][(k - 1) % 3] + 1
            if (
                graph[i][j] == k
                and j - 1 >= 0
                and d[i][j][k] < d[i][j - 1][(k - 1) % 3] + 1
            ):
                d[i][j][k] = d[i][j - 1][(k - 1) % 3] + 1
print(max(d[N - 1][N - 1]))
"""
4
0 1 2 2
1 1 1 1
2 2 2 2
0 0 1 0
"""