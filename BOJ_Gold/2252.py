import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline


# 줄세우기 - 위상정렬 기본문제

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 인접 리스트
outDeg = [0 for _ in range(N+1)]  # 0 사용 X
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    outDeg[v] += 1
q = []
for i in range(1, N+1):  # 진입차수 0 인경우 q에 넣는다.
    if outDeg[i] == 0:
        q.append(i)

# 모든 정점 순회 , 다 돌기전에 빈큐가 있다면 싸이클이 있는것!
for i in range(1, N+1):
    if not q:
        print(f"싸이클 생성")
        break
    # 큐에서 인접노드의 진입차수를 제거 후 , 0이된 노드를 큐에 넣는다.
    now = q.pop(0)
    print(f"{now} ", end="")
    for nxt in graph[now]:
        outDeg[nxt] -= 1
        if outDeg[nxt] == 0:
            q.append(nxt)
