

import sys
import math

# 플로이드 와샬 알고리즘
# 모든 정점으로부터 모든 정점까지 최단거리
# 자료구조 : 거리 인접행렬
# 알고리즘 : 1 간선의 정보로 먼저 거리 인접행렬 업데이트
# 2. i - k - j 을 순회하며, k를 거쳐가는 경우 , 더 짧은 경로가 발견된다면
# dist[i][j]를 업데이트

input = sys.stdin.readline

N = int(input())
M = int(input())
dist = [[math.inf for _ in range(N+1)] for _ in range(N+1)]
# 거리 테이블을 작성
for _ in range(M):
    u, v, w = map(int, input().split(" "))
    # ❌ 초기 거리값도 최소로 넣어야 한다.
    dist[u][v] = min(dist[u][v], w)

for i in range(1, N+1):
    dist[i][i] = 0
# i -> k -> j 로 가는 경우를 명시
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            newDist = dist[i][k] + dist[k][j]
            dist[i][j] = min(dist[i][j], newDist)


for d in dist[1:]:
    print(*map(lambda x: 0 if x == math.inf else x, d[1:]))
