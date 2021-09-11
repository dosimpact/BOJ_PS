
# 지점의 갯수, 시작, 목표지점 a,b, fares
INF = 4000000


def solution(n, s, a, b, fares):
    # 거리 배열은 inf 로 초기화
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    # dist 행렬 초기화
    for u, v, w in fares:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    # 제자리 걸음
    for i in range(1, n+1):
        dist[i][i] = 0
    # dist 행렬 와샬
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or i == k or k == j:
                    continue
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
    # 최소값 답
    minAns = INF
    for k in range(1, n+1):
        minAns = min(minAns, dist[s][k] + dist[k][a] + dist[k][b])

    return minAns
