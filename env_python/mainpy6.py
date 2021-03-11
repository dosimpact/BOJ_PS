import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

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

wallCount = 0
minSpread = N*M
initStart = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            initStart.append((i, j))
        if graph[i][j] == 1:
            wallCount += 1


def BFS():
    global minSpread
    check = [[False for _ in range(M)] for _ in range(N)]
    dq = deque()
    count = 0
    for init in initStart:
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
            if count >= minSpread:
                return
            dq.append((nx, ny))
    minSpread = count


for x1 in range(N):
    for y1 in range(M):

        if graph[x1][y1] != 0:
            continue
        graph[x1][y1] = 1
        for x2 in range(N):
            for y2 in range(M):

                if x1 == x2 and y1 == y2:
                    continue
                if graph[x2][y2] != 0:
                    continue
                graph[x2][y2] = 1
                for x3 in range(N):
                    for y3 in range(M):

                        if x2 == x3 and y2 == y3:
                            continue
                        if graph[x3][y3] != 0:
                            continue
                        graph[x3][y3] = 1
                        BFS()
                        graph[x3][y3] = 0
                graph[x2][y2] = 0
        graph[x1][y1] = 0

print(N*M - minSpread - wallCount-3)
