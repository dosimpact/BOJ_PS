import sys
import math
import re
import heapq
from typing import *

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for i in range(V+1)]  # 0 unused,1...V
check = [False for _ in range(V+1)]
pq = []  # 가중치,다음노드

for _ in range(E):

    u, v, w = map(int, input().split())
    if _ == 0:
        pq.append((0, u))
    graph[u].append((v, w))
    graph[v].append((u, w))  # FB 💥 양방향 그래프이어야함!!

ans = 0
# print(graph)
heapq.heapify(pq)
while pq:
    w, now = heapq.heappop(pq)
    # print(f" w now => {w} {now} | {pq}")
    if check[now]:
        continue
    check[now] = True  # 방문 후 , 다음 최소 가중치를 방문 및 주변 간선 푸쉬
    ans += w
    for nxt, nxt_w in (graph[now]):
        heapq.heappush(pq, (nxt_w, nxt))

print(ans)
"""
3 3
1 2 -1
2 3 -2
1 3 -3

-5
"""
"""
9 20
1 2 4
2 3 2
1 4 1
2 5 6
3 6 5
2 4 2
1 5 8
2 6 1
3 5 2
4 5 11
5 6 3
4 7 9
5 8 1
6 9 8
7 8 6
8 9 3
5 7 4
4 8 8
5 9 5
6 8 7

16
"""
