import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[]for _ in range(N+1)]
    for __ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(N-1)
