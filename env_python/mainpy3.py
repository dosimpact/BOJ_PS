import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


V, E = map(int, input().split())
graph = [i for i in range(V+1)]  # 1,2,3 (0 unused)
ETable = [list(map(int, input().split())) for _ in range(E)]
ETable.sort(key=lambda x: x[2])

# print(ETable)


def getP(x: int):
    if graph[x] == x:
        return x
    graph[x] = getP(graph[x])
    return graph[x]


def graph_union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px > py:  # 5 3
        graph[px] = py   # 아래 5 가  3으로 연결
    else:
        graph[py] = px


def graph_find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


ans = 0
cnt = 0
for i in range(len(ETable)):
    if cnt == V-1:
        break
    x, y, w = ETable[i]
    if not graph_find(x, y):
        graph_union(x, y)
        ans, cnt = ans + w, cnt+1
    # print(f"i {i} {graph} ", x, y, w)
print(ans)

"""
5 7
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1
4 5 2
5
"""
