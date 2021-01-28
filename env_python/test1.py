import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 그래프 BFS /DFS 탐색 문제
# 작은 정점부터 방문
N, M, START = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 그래프 입력 > 인접 리스트
for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

for i in range(N):
    graph[i].sort()

check = [0]*(N+1)

# DFS 를 먼저 돌자.


def DFS(now: int):
    check[now] = 1
    print(now, end=" ")
    # 주변 탐색
    for next in graph[now]:
        if check[next] == 0:
            DFS(next)


DFS(START)
check = [0]*(N+1)
# BFS 를 돌자

print()


def BFS(s: int):
    check[s] = 1
    q = [s]
    print(s, end=" ")
    while q:
        now = q.pop(0)
        for nxt in graph[now]:
            if check[nxt] == 0:
                print(nxt, end=" ")
                check[nxt] = 1
                q += [nxt]


BFS(START)
