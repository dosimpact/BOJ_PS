import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())  # 총 도시 수
M = int(input())  # 여행에 속한 도시들의 수
graph = [list(map(int, input().split())) for _ in range(N)]  # 인접행렬
# print(graph)
dest = list(map(lambda x: int(x)-1, input().split()))  # 목표 도시 , -1 씩 했음


parent = [i for i in range(N)]  # 0,1,2,
# ---


def getP(x: int):
    if parent[x] == x:
        return x
    parent[x] = getP(parent[x])
    return parent[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if graph[i][j] == 1:
            union(i, j)
            # print(parent)

ans = True
for i in range(len(dest)-1):
    if not find(dest[i], dest[i+1]):
        ans = False
print("YES") if ans else print("NO")

"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3

2
1
0 1
1 0
1

2
1
0 0
0 0
1

2
1
0 0
0 0
1 2
"""
