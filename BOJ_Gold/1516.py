import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
buildUp = [0 for _ in range(N+1)]
inDeg = [0 for _ in range(N+1)]
for u in range(1, N+1):
    data = list(map(int, input().split()))
    buildUp[u] = data[0]
    data = data[1:-1]
    for v in data:
        graph[v].append(u)  # v -> u
        inDeg[u] += 1  # u +=1
#  건물들의 순서 - 위상정렬로 방문한다.
# 방문시 그 전의 build (가중치) 만큼 check를 늘려준다.
q = []
for i in range(1, N+1):
    if inDeg[i] == 0:
        q.append(i)
        check[i] = buildUp[i]

while q:
    now = q.pop(0)  # 현재 노드를 방문 | 인접 노드 차수 때기 | 0 인경우 -큐에넣고,check업데이트
    for nxt in graph[now]:
        inDeg[nxt] -= 1
        check[nxt] = max(check[nxt], check[now])
        if inDeg[nxt] == 0:
            check[nxt] += buildUp[nxt]
            q.append(nxt)

for c in check[1:]:
    print(c)

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

5
10 -1
20 1 -1
30 1 -1
10 1 -1
10 2 4 -1
>
10
30
40
20
30 ❌ > 40
"""
