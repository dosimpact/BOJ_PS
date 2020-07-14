

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
check = [[[-1 for _ in range(2)] for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


def BFS(x: int, y: int):
    global check
    check[x][y][0] = 0
    q = [(x, y, 0)]
    while q:
        x, y, z = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not inRange(nx, ny) or check[nx][ny][z] != -1:
                continue
            if(z == 0):  # CASE 1 현재 벽을 안부순 경우 탐색
                # CASE 1-1벽을 안부수고 계속탐색
                if graph[nx][ny] == 0:
                    check[nx][ny][0] = check[x][y][0]+1
                    q.append((nx, ny, 0,))
                # CASE 1-2 벽을 부수고 계속 탐색
                if graph[nx][ny] == 1:
                    check[nx][ny][1] = check[x][y][0]+1
                    q.append((nx, ny, 1,))
            else:  # CASE 2 현재 벽을 부순 경우 탐색
                # CASE 2 벽을 안부수고 계속 탐색
                if graph[nx][ny] == 0:
                    check[nx][ny][z] = check[x][y][z]+1
                    q.append((nx, ny, z,))


BFS(0, 0)

u, v = check[N-1][M-1][0], check[N-1][M-1][1]
if u == v == -1:
    print(-1)
else:
    if u == -1:
        print(v+1)
    elif v == -1:
        print(u+1)
    else:
        print(min(u+1, v+1))
"""
1 1
0

2 2
01
10

6 4
0100
1110
1000
0000
0111
0000
"""
