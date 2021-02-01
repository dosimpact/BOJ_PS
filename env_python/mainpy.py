import sys
import math
from typing import *

sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


input = sys.stdin.readline


N, E, S_N = map(int, input().split())
graph: List[List[int]] = [[] for _ in range(N+1)]

for i in range(E):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

for row in graph:
    row.sort()


check = [0 for _ in range(N+1)]


def DFS(x: int):
    # x 방문,체크,출력
    check[x] = 1
    print(x, end=" ")
    # 다음 탐색
    for next_node in graph[x]:
        if check[next_node] == 0:
            DFS(next_node)


DFS(S_N)
check = [0 for _ in range(N+1)]
print()


def BFS(x: int):
    # x 방문 체크
    # 큐 생성 및 넣기 (방문 체크하고 넣는다.)
    check[x] = 1
    print(x, end=" ")
    q = [x]
    # 다음 노트 탐색
    while q:
        now_node = q.pop(0)
        for next_node in graph[now_node]:
            if check[next_node] == 0:
                check[next_node] = 1
                print(next_node, end=" ")
                q += [next_node]


BFS(S_N)

"""
4 5 1
1 4
1 3
1 2
2 4
3 4
"""
