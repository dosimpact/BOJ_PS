import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 3차원 BFS
dL = [1, 0, 0, -1, 0, 0]
dR = [0, 1, 0, 0, -1, 0]
dC = [0, 0, 1, 0, 0, -1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        sys.exit(0)

    graph = []
    check = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for l in range(L):  # 층
        floor = []
        for r in range(R):  # 열마다
            floor.append(list(input().strip()))
        input()
        graph.append(floor)

    start_point = None
    q = []
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    start_point = (i, j, k)
                    check[i][j][k] = 1
                    q.append((i, j, k))
    isEsc = False
    while q and not isEsc:
        now_L, now_R, now_C = q.pop(0)
        for i in range(6):  # 다음 노드
            nxt_L, nxt_R, nxt_C = now_L+dL[i], now_R+dR[i], now_C+dC[i]
            if nxt_L < 0 or nxt_L >= L or nxt_R < 0 or nxt_R >= R or nxt_C < 0 or nxt_C >= C:
                continue
            if check[nxt_L][nxt_R][nxt_C] != 0:
                continue
            if graph[nxt_L][nxt_R][nxt_C] == "#":
                continue
            if graph[nxt_L][nxt_R][nxt_C] == ".":
                check[nxt_L][nxt_R][nxt_C] = check[now_L][now_R][now_C]+1
                q.append((nxt_L, nxt_R, nxt_C))
            if graph[nxt_L][nxt_R][nxt_C] == "E":
                print(f"Escaped in {check[now_L][now_R][now_C]} minute(s).")
                isEsc = True
    if not isEsc:
        print("Trapped!")
