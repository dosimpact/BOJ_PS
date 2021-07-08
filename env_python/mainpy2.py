import sys


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# inputs , 정점, 간선 , 시작 노드 번호
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 0 unused
check = [False for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

# sort
for i in range(N):
    graph[i].sort()

# dfs
def DFS(x: int):
    print(x, end=" ")
    for nxt in graph[x]:
        if check[nxt] == False:
            check[nxt] = True
            DFS(nxt)


check[V] = True
DFS(V)
print()
check = [False for _ in range(N + 1)]
# bfs
def BFS(x: int):
    q = []
    check[x] = True
    q.append(x)
    print(x, end=" ")
    while q:
        now = q.pop(0)
        for nxt in graph[now]:
            if check[nxt] == False:
                check[nxt] = True
                print(nxt, end=" ")
                q.append(nxt)


BFS(V)

