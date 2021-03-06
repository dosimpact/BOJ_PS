import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline


# 수행해야할 작업 N 개
# 작업간의 선행 관계
# 모든 작업을 하기 위한 최소 시간 - check = max(연동된 전작업)
N = int(input())
graph = [[] for _ in range(N+1)]  # 0 은 사용 X
check = [0 for _ in range(N+1)]
inDeg = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    data = data[2:]
    for u in data:  # u -> i
        graph[u].append(i)
        inDeg[i] += 1
q = []
for i in range(1, N+1):
    if inDeg[i] == 0:
        q.append(i)
        check[i] = time[i]

while q:
    now = q.pop(0)
    for nxt in graph[now]:
        inDeg[nxt] -= 1
        check[nxt] = max(check[nxt], check[now])
        if inDeg[nxt] == 0:
            check[nxt] += time[nxt]
            q.append(nxt)

print(max(check))
