from sys import stdin, setrecursionlimit
from collections import deque, defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)

# 위상 정렬, 인접리스트 + inDeg counter , inDeg==0 이면 방문 순회 및 간선 제거
V, E = map(int, input().split())  # V,E
graph = [[] for _ in range(V + 1)]  # 0 unuse
inDeg = [0 for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    inDeg[v] += 1
    graph[u].append(v)

q = []
for i in range(1, V + 1):
    if inDeg[i] == 0:
        q.append(i)

for i in range(1, V + 1):
    now = q.pop(0)
    print(now, end=" ")
    for nxt in graph[now]:
        inDeg[nxt] -= 1
        if inDeg[nxt] == 0:
            q.append(nxt)
