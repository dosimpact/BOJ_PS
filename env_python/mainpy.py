import sys


def input():
    return sys.stdin.readline().rstrip()


n, m, v = map(int, input().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]
# 인접 행렬로

# graph 채우기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def DFS(x: int):
    global check
    check[x] = 1
    print(x, end=" ")
    # 주변 노드 탐색
    for idx in range(len(graph[x])):
        if graph[x][idx] == 1 and check[idx] == 0:
            DFS(idx)


def BFS(x: int):
    global check
    check[x] = 1
    print(x, end=" ")
    q = [x]
    while q:
        now = q.pop(0)
        for idx in range(len(graph[now])):
            if graph[now][idx] == 1 and check[idx] == 0:
                check[idx] = 1
                print(idx, end=" ")
                q.append(idx)


DFS(v)
check = [0 for _ in range(n + 1)]
print()
BFS(v)
"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
