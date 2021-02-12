import sys
import math
import re
from typing import *

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [i for i in range(V+1)]  # 0 unused,1...V
ETable = [list(map(int, input().split())) for _ in range(E)]
ETable.sort(key=lambda x: x[2])  # w sort
# MST 문제 - UnionFind


def graph_getP(x: int):
    if graph[x] == x:
        return x
    graph[x] = graph_getP(graph[x])
    return graph[x]


def graph_union(x: int, y: int):
    px, py = graph_getP(x), graph_getP(y)
    if px > py:  # 5 3
        graph[px] = py
    else:
        graph[py] = px


def graph_find(x: int, y: int):
    px, py = graph_getP(x), graph_getP(y)
    return px == py


ans = 0
for i in range(len(ETable)):
    x, y, w = ETable[i]
    if not graph_find(x, y):
        graph_union(x, y)
        ans += w


print(ans)
