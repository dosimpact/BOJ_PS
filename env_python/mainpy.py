import sys
import itertools
import heapq
from collections import deque

input = sys.stdin.readline

M, N, V = map(int, input().split())
X, Y = map(int, input().split())
X, Y = X-1, Y-1
graph_h = [list(map(int, input().split())) for _ in range(M)]  # 높이에 대한 그래프
fire = [list(map(int, input().split())) for _ in range(V)]
fire.sort(key=lambda x: x[2])
# -1 방문 X , 0 이면 화산, 4면 4초에 덮인다
check_f = [[-1 for _ in range(N)] for _ in range(M)]
check_p = [[-1 for _ in range(N)] for _ in range(M)]
graph_m = [[False for _ in range(N)] for _ in range(M)]

q_fire = []  # 시간, 위치, 위치
heapq.heapify(q_fire)
for (fx, fy, ft) in (fire):
    graph_m[fx-1][fy-1] = True
    # check_f[fx-1][fy-1] = ft
    heapq.heappush(q_fire, (ft, fx-1, fy-1))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def inRange(x: int, y: int):
    return (x >= 0 and y >= 0 and x < M and y < N)


def printG(g):
    for gr in g:
        print(gr)


for time in range(0, max(M, N) + 500):
    while q_fire and q_fire[0][0] <= time:
        ft, fx, fy = heapq.heappop(q_fire)
        for k in range(4):
            nt, ny, nx = ft+1, fx+dx[k], fy+dy[k]
            if inRange(ny, nx) and check_f[ny][nx] == -1:
                check_f[ny][nx] = ft+1
                heapq.heappush(q_fire, (nt, ny, nx))


# 이동 BFS 큐 - 1 씩 check 증가
check_p[X][Y] = 0
q = [(X, Y)]
ans = [(graph_h[X][Y], 0)]
while q:
    x, y = q.pop(0)
    for k in range(4):
        nx, ny = x+dx[k], y + dy[k]
        if not inRange(nx, ny):
            continue
        if check_p[nx][ny] != -1:
            continue
        if graph_m[nx][ny]:
            continue
        if check_f[nx][ny] <= check_p[x][y]+1:
            continue
        check_p[nx][ny] = check_p[x][y]+1
        q.append((nx, ny))
        ans.append((graph_h[nx][ny], check_p[nx][ny]))

ans.sort(key=lambda x: x[0], reverse=True)
print(ans[0][0], ans[0][1])
"""
4 4 4
2 4
5 3 3 2 
4 6 6 4
6 3 6 1 
2 3 6 4
1 1 4
1 2 4
3 4 2
4 4 3

3 3 2
1 1
0 0 9
0 0 0
0 0 0
2 3 9
3 3 0
"""
