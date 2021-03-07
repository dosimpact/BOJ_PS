import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil


# 첫번쨰거울에서 시작 , (방향,위치,튕긴거울수) - whle문 돌려,
N = int(input())
graph = [list(input()) for _ in range(N)]
check = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]
endpoints = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == "#":
            endpoints += [i, j]

sx, sy, fx, fy = endpoints
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
q = deque()  # 튕긴 거울의 수|좌표|현재 나가는 방향

for k in range(4):
    q.append([0, sx, sy, k])
    check[sx][sy][k] = 1


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < N


# 빈공간 - 계속 , 벽,out of range - stop, 거울 - 양갈래로 직진 큐 생성
# 무한 루프를 도는 빛이 있으므로 최단거리로 이동을 살펴야한다.
while q:
    w, x, y, di = q.popleft()
    while True:  # 빛의 이동
        nx, ny = x+dx[di], y+dy[di]
        if not inRange(nx, ny):
            break
        if graph[nx][ny] == "*":
            break
        if graph[nx][ny] == "#":
            # print(f"END : {nx,ny,w,di}")
            if (nx == fx and ny == fy):
                print(w)
                exit(0)
        if graph[nx][ny] == "!":
            ndi = (di+1) % 4
            if check[nx][ny][ndi] == -1:
                q.append((w+1, nx, ny, ndi))
                check[nx][ny][(di+1) % 4] = check[x][y][di]+1
            ndi = (di-1) % 4
            if check[nx][ny][ndi] == -1:
                q.append((w+1, nx, ny, ndi))
                check[nx][ny][(di+1) % 4] = check[x][y][di]+1
        x, y = nx, ny

"""
5
***#*
*.!.*
*!.!*
*.!.*
*#***
>2

5
*#***
*.!.*
*!.!*
*.!.*
*#***
>

5
*****
*!!.#
*!.!*
*!!.*
*#***
>1

5
.....
!...#
.....
.*...
!#...
>2

5
.#...
!!...
.....
.*...
!#...
>3

5
.#...
.!..!
.....
.!..!
.#...
>4

9
.!*......
..!.!*!.!
# .!*.*.*.
!!.*!.!*.
.*.......
.#......!
.........
.........
!.......!
>3

❌
- 비친 문이 알고보니 자기자신..
7
!!..!.#
*.....*
.!..!..
!!*.!.!
.*!!.*!
...!!..
!*#****
>5

❌
- 시간 초과
10
****#*****
!!..!.!..!
......*...
......!..!
*!....!..*
......!..!
.!....!...
...!*.*...
!..!!.!..!
****#*****
>8
"""
