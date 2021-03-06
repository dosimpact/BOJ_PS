import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 1..N 문제 - 난이도 순서
# 가능한 쉬운문제 부터, 먼저푸는것이 좋은 문제
# q 순위
# 1. 위상정렬 조건 -> inDegree 0 조건
# 2. 문제 난이도 조건  -> 우선순위 큐

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDeg = [0 for _ in range(N+1)]  # 0 사용 X
for _ in range(M):
    u, v = map(int, input().split())  # 4->2
    graph[u].append(v)
    inDeg[v] += 1
pq = []
for i in range(1, N+1):  # 1번 노드 ~ 4번 노드
    if inDeg[i] == 0:
        heapq.heappush(pq, i)

while pq:
    now = heapq.heappop(pq)
    print(now, end=" ")
    for nxt in graph[now]:
        inDeg[nxt] -= 1
        if inDeg[nxt] == 0:
            heapq.heappush(pq, nxt)
