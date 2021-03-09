import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil
from itertools import product, combinations

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


# 연구소 빈칸,벽, 바이러스 - 한칸씩 버짐
# 3개의 벽 - BF,안전영역 최댓값
"""
리팩토링
- 구지 for 6중 돌려야 하나?
> 빈공간에 대한 filter 후 조합 만들기
"""

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

viruss = list(filter(lambda x: graph[x[0]]
                     [x[1]] == 2, product(range(N), range(M))))
emptys = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 0]
walls = list(filter(lambda x: graph[x[0]]
                    [x[1]] == 1, product(range(N), range(M))))
maxSpreaded = N*M


def BFS2():
    global maxSpreaded
    check = [[False for _ in range(M)] for _ in range(N)]
    dq = deque()
    count = 0
    for init in viruss:
        x, y = init
        count += 1
        check[x][y] = True
        dq.append((x, y))
    while dq:
        x, y = dq.popleft()  # 현재 위치
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            nx, ny = x+dx, y+dy
            if not(nx >= 0 and ny >= 0 and nx < N and ny < M):
                continue
            if check[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            check[nx][ny] = True
            count += 1
            if count >= maxSpreaded:
                return
            dq.append((nx, ny))
    maxSpreaded = count


for case in combinations(emptys, 3):
    for vx, vy in case:
        graph[vx][vy] = 1
    BFS2()
    for vx, vy in case:
        graph[vx][vy] = 0

print(N*M - (maxSpreaded) - len(walls) - 3)
