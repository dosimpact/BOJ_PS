import sys
import math
import re
import heapq
from typing import *

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 프림 알고리즘

N = int(input())
starts: List[List[float]] = [
    list(map(float, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
check = [False for _ in range(N)]


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        graph[i].append((j, dist(starts[i], starts[j])))

# print(graph)
pq = [(0, 0)]  # 가중치,다음 노드 넘버
heapq.heapify(pq)
ans = 0
while pq:
    w, now = heapq.heappop(pq)  # 힙큐에서 꺼내온다.
    if check[now]:
        continue
    # 해당 노드를 방문해서 가중치 인정 및 방문 체크
    ans += w
    check[now] = True
    for nxt, nxt_w in graph[now]:
        if not check[nxt]:
            heapq.heappush(pq, (nxt_w, nxt))
print(ans)
