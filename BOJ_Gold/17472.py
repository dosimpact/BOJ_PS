import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


def BFS(node, I):
    IPoints[I].append((node[0], node[1]))
    check[node[0]][node[1]] = I
    q = [(node[0], node[1])]
    while q:
        now_x, now_y = q.pop(0)
        for k in range(4):  # 4방향 탐색,갈수있는지,범위치크
            nxt_x, nxt_y = now_x+dx[k], now_y+dy[k]
            if inRange(nxt_x, nxt_y) and graph[nxt_x][nxt_y] == 1 and check[nxt_x][nxt_y] == 0:
                check[nxt_x][nxt_y] = I
                IPoints[I].append((nxt_x, nxt_y))
                q.append((nxt_x, nxt_y))
    return


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
check = [[0 for _ in range(M)] for _ in range(N)]

I = 0  # 섬의수
IPoints = [[]]  # 해당 섬의 좌표들 ( 0 안사용 )
q = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and check[i][j] == 0:
            I += 1
            IPoints.append([])
            BFS((i, j), I)

# 크루스칼 알고리즘 사용
parents = [i for i in range(I+1)]  # 4개의 섬 사용 ( 0 사용 X )
edges: List[List[int]] = []  # 모든 간선을 가져온다. (시작섬,도착섬,거리)


def getP(x: int):
    if x == parents[x]:
        return x
    parents[x] = getP(parents[x])
    return parents[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px > py:
        parents[px] = py
    else:
        parents[py] = px


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


def dist(p1, p2):
    # 추가 검사, 가는길에 grpah=0 으로 바다만 있어야함.
    if p1[0] == p2[0]:  # 세로 다리
        x = p1[0]
        u, v = min(p1[1], p2[1]), max(p1[1], p2[1])
        for y in range(u+1, v):
            if graph[x][y] != 0:
                return 0
    if p1[1] == p2[1]:  # x축 방향 다리
        y = p1[1]
        u, v = min(p1[0], p2[0]), max(p1[0], p2[0])
        for x in range(u+1, v):
            if graph[x][y] != 0:
                return 0
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])


for i in range(1, I+1):
    for j in range(1, I+1):
        if i == j:
            continue
        # i 에 속한 모든 섬에서 , j 에 속한 모든 섬정점 으로부터 edge를 다 더한다.
        for p1 in IPoints[i]:
            for p2 in IPoints[j]:
                if p1[0] != p2[0] and p1[1] != p2[1]:  # 가로 or 세로 다리가 안되는경우
                    continue
                d = dist(p1, p2)-1
                if d <= 1:
                    continue
                edges.append((i, j, d))
edges.sort(key=lambda x: x[2])
# 가능한 간선은 같은 행 혹은 열에 존재하는 다른 섬들이다.
cnt = 1
ans = 0
for i in range(len(edges)):
    u, v, w = edges[i]
    if not find(u, v):
        union(u, v)
        ans += w
        cnt += 1
if cnt == I:
    print(ans)
else:
    print(-1)
