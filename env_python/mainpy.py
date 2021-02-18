import sys
import math
import re
import heapq
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]  # 0 un use
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

check = [False for _ in range(V + 1)]
dist = [math.inf for _ in range(V + 1)]
pq = [(0, K)]
heapq.heapify(pq)  # 거리 , 다음 노드 정보
dist[K] = 0

while pq:
    now_w, now = heapq.heappop(pq)  # 현재 노드에서 탐색
    if check[now]:
        continue
    check[now] = True
    for nxt, nxt_w in graph[now]:  # 다음노드로 가는 거리 계산 후 갱신 , 엔큐
        if dist[nxt] > dist[now] + nxt_w:
            dist[nxt] = dist[now] + nxt_w
            heapq.heappush(pq, (dist[nxt], nxt)) # dist중에서 최소 + 아직 방문하지 않은 점이 다음 목표임
            # heapq.heappush(pq, (nxt_w, nxt))

for d in dist[1:]:
    if d == math.inf:
        print("INF")
    else:
        print(d)