import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())  # 1~N
S, E = map(int, input().split())  # start end
tels = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    tels[u].append(v)
    tels[v].append(u)
check = [-1 for _ in range(N+1)]
q = deque()
q.append(S)
check[S] = 0
while q:
    now = q.popleft()
    if now == E:
        print(check[E])
        break
    # 다음 노드 방문
    if now-1 >= 1 and check[now-1] == -1:
        check[now-1] = check[now]+1
        q.append(now-1)
    if now+1 <= N and check[now+1] == -1:
        check[now+1] = check[now]+1
        q.append(now+1)
    for nxt in tels[now]:
        if check[nxt] == -1:
            check[nxt] = check[now]+1
            q.append(nxt)


"""
10 3
2 5
1 6
1 3
2 8
"""
