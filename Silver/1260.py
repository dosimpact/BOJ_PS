
import sys


def input(): return sys.stdin.readline().rstrip()


def bfs(v):
    global check, graph
    check[v] = 1
    print(v, end=' ')
    for e in graph[v]:
        if check[e] == 0:
            check[e] = 1
            bfs(e)


def dfs(v):
    global check, graph
    check[v] = 1
    print(v, end=' ')
    q = []
    q.append(v)
    while len(q) != 0:
        now = q.pop(0)
        for e in graph[now]:
            if check[e] == 0:
                check[e] = 1
                print(e, end=' ')
                q.append(e)


(N, M, V) = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    (u, v) = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

check = [0 for _ in range(N+1)]
bfs(V)
print()
check = [0 for _ in range(N+1)]
dfs(V)
