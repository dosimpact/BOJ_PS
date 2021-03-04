import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline


# 선수과목
# 총 몇 학기가 걸리는가?
N, M = map(int, input().split())  # N개의 노드 , 0사용 X
graph = [[] for _ in range(N+1)]  # 인접 행렬
check = [0 for _ in range(N+1)]  # 방문 순서 체크 ( BFS 요소 넣음)
inDeg = [0 for _ in range(N+1)]  # 출입 차수
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    inDeg[v] += 1
q = []
# inDeg가 0 인것, check 1로 만들고 큐에 넣기
for i in range(1, N+1):
    if inDeg[i] == 0:
        check[i] = 1
        q.append(i)

while q:
    now = q.pop(0)
    for nxt in graph[now]:  # 인접한 노드 탐색 | 차수 제거 | 0 이면 넣기 check 하고
        inDeg[nxt] -= 1
        if inDeg[nxt] == 0:
            q.append(nxt)
            check[nxt] = check[now]+1

print(*check[1:])
