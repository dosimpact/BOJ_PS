from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# 싸이클 찾고, 싸이클이 아닌 노드에서 싸이클까지 거리
# 차수를 탐색하는 문제
N = int(input())
graph = [[] for _ in range(N+1)]  # 0 unused
for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# ❌ 반드시 3차만 분기점이 아니다.
# - 차수와 분기점은 상관없드라.
degree_1 = []
degree_j = []
for idx, row in enumerate(graph):
    if len(row) == 1:
        degree_1.append(idx)
    if len(row) >= 3:
        degree_j.append(idx)
print(graph)
print(degree_1, degree_j)
# 끝점에서 BFS 시작 -1
dist = [0 for _ in range(N+1)]
check = [False for _ in range(N+1)]
dq = deque()

for s in degree_1:
    check[s] = True
    dq.append(s)
while dq:
    now = dq.popleft()
    for nxt in graph[now]:
        if check[nxt]:
            continue
        if nxt in degree_j:
            continue
        check[nxt] = True
        dq.append(nxt)
print(check)
# 분기점에서 BFS 시작 -2
for s in degree_j:
    dq.append(s)
while dq:
    now = dq.popleft()
    for nxt in graph[now]:
        if dist[nxt] != 0:
            continue
        if check[nxt] == False:
            continue
        if dist[nxt] != 0:
            continue
        dist[nxt] = dist[now]+1
        dq.append(nxt)
print(*dist[1:])
# 분기점과의 최소값 출력


"""
6
1 2
3 4
6 4
2 3
1 3
3 5
"""
