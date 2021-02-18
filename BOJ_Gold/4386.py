import sys
import math
import re
import heapq
from typing import *

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]
edges: Tuple[int, int, float] = []
parents = [i for i in range(N)]


def getP(x: int):
    if parents[x] == x:
        return x
    parents[x] = getP(parents[x])
    return parents[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px > py:  # 5 3
        parents[px] = py
    else:
        parents[py] = px


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


for i in range(len(stars)):
    for j in range(len(stars)):
        if i == j:
            continue
        edges.append((i, j, dist(stars[i], stars[j])))
edges.sort(key=lambda x: x[2])

ans = 0
for i in range(len(edges)):
    u, v, w = edges[i]
    # print(f" u v w {u} {v} {w}")
    if not find(u, v):
        union(u, v)
        ans += w
print(ans)
