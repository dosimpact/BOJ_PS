import sys

input = sys.stdin.readline

# dfs,bfs 탐색 결과
# 작은 정점부터 탐색
# 1~N

# 정점수, 간선수, 탐색 시작 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
check = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N + 1):
    graph[i].sort()

# DFS
def DFS(x: int):
    print(x, end=" ")
    for nxt in graph[x]:
        if check[nxt]:
            continue
        check[nxt] = True
        DFS(nxt)


check[V] = True
DFS(V)
print()

# BFS

check = [False for _ in range(N + 1)]
q = []
q.append(V)
check[V] = True
print(V, end=" ")
while q:
    now = q.pop(0)
    for nxt in graph[now]:
        if not check[nxt]:
            check[nxt] = True
            print(nxt, end=" ")
            q.append(nxt)
