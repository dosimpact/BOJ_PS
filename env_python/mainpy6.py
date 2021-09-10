res = "+".join("hello")
print(res)
res = "+".join(map(str, [1, 2, 3]))
print(res)
import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = float("inf")

N = int(input())
graph = []
# [N][2**N] = [현재노드][방문상태]
cache = [[INF for _ in range(2 ** N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))


def TSP(current: int, visited: int):
    # basecase 모든 정점방문 -> 0번으로 돌아가
    if visited == (1 << N) - 1:  # == (2**N)-1
        return graph[current][0] or INF

    # 캐쉬 - 현재상태에서 최적값이 캐쉬 있다면 바로 리턴
    if cache[current][visited] != INF:
        return cache[current][visited]
    # 다음 경로를 재귀 호출
    tmp = INF
    for i in range(N):
        if graph[current][i] == 0:  # 가는 경로가 없다면
            continue
        if visited & (1 << i):
            continue
        tmp = min(tmp, TSP(i, visited | (1 << i)) + graph[current][i])
    cache[current][visited] = tmp
    return tmp


print(TSP(0, 1 << 0))

"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""
