import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [i for i in range(0, N+1)]  # N+1개이다.


def get_parent(x: int):
    if graph[x] == x:
        return x
    graph[x] = get_parent(graph[x])
    return graph[x]


def graph_union(x: int, y: int):
    px = get_parent(x)
    py = get_parent(y)
    if px > py:
        graph[px] = py
    else:
        graph[py] = px


def graph_find(x: int, y: int):
    px = get_parent(x)
    py = get_parent(y)
    return px == py


for _ in range(M):
    c, x, y = map(int, input().split())
    if c == 0:
        graph_union(x, y)
    else:
        if graph_find(x, y):
            print("YES")
        else:
            print("NO")
