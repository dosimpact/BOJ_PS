import sys
import math


# 자신의 수색 범위가 있다.
# 얻을 수 있는 최대 갯수
# 다익스트라 여러번
# 플로이드 와샬 + 반복

# 지역갯수, 수색범위, 길의 갯수
N, M, R = map(int, input().split())
items = list(map(int, input().split()))
dist = [[math.inf for _ in range(N + 1)] for _ in range(N + 1)]

for r in range(R):
    u, v, w = map(int, input().split())
    dist[u][v] = w
    dist[v][u] = w

for i in range(1, N + 1):
    dist[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

tmpAns = []
for i in range(1, N + 1):
    tmp = 0
    for j in range(1, N + 1):
        if dist[i][j] <= M:
            tmp += items[j - 1]
    tmpAns.append(tmp)
print(max(tmpAns))