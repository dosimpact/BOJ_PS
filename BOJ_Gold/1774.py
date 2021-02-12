import sys
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


def getP(x: int):
    if parents[x] == x:
        return x
    parents[x] = getP(parents[x])
    return parents[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px > py:
        parents[px] = py
    else:
        parents[py] = px


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


N, M = map(int, input().split())
# 0 사용 X , 각 노드의 위치
points = [list(map(float, input().split()))for _ in range(N)]
points = [[0, 0]] + points
# 미리 연결된 노드
node_connected = [list(map(int, input().split())) for _ in range(M)]

parents = [i for i in range(N+1)]  # N개의 정점의 부모 ( 0 사용 X )
ans = 0
for i in range(len(node_connected)):
    u, v = node_connected[i]
    union(u, v)
    # ans += dist(points[u], points[v])

# 모든 간선에대해, 크루스칼 적용
edges = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue
        edges.append((i, j, dist(points[i], points[j])))
edges.sort(key=lambda x: x[2])
for i in range(len(edges)):
    u, v, w = edges[i]
    if not find(u, v):
        union(u, v)
        ans += w

# print("%.2f" % ans)
print(round(ans, 2))
