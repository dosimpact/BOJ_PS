import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil
from itertools import combinations

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

# 빈 필드, # 울타리, o 양, v늑대
# BFS 탐색 - 컴포넌트의 수
# 빈공간이면 탐색을 시작한다.
# 범위 밖이거나, 울타리라면 이동 불가, 컴포넌트를 다 돌고나면 늑대의 수 양의 수 리턴

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
check = [[-1 for _ in range(M)] for _ in range(N)]


def BFS(x: int, y: int, c: int):
    v, o = 0, 0
    dq = deque()
    if graph[x][y] == "v":
        v += 1
    if graph[x][y] == "o":
        o += 1
    dq.append((x, y))
    check[x][y] = c
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            nx, ny = x+dx, y+dy
            if not (nx >= 0 and ny >= 0 and nx < N and ny < M):
                continue
            if graph[nx][ny] == "#":
                continue
            if check[nx][ny] != -1:
                continue
            if graph[nx][ny] == "v":
                v += 1
            if graph[nx][ny] == "o":
                o += 1
            check[nx][ny] = check[x][y]
            dq.append((nx, ny))
    return (o, v)


ansO, ansV = 0, 0
cnt = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] != "#" and check[i][j] == -1:
            o, v = BFS(i, j, cnt)  # 양 과 늑대
            if o == v:
                ansV += o
            elif o < v:
                ansV += v
            else:
                ansO += o
            cnt += 1
print(ansO, ansV)
"""
9 12
.###.#####..
# .oo#...#v#.
# ..o#.#.#.#.
# ..##o#...#.
# .#v#o###.#.
# ..#v#....#.
# ...v#v####.
.####.#vv.o#
.......####.
"""
