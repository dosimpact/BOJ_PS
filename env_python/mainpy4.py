# import sys
# import heapq
# import re
# import math
# from collections import deque
# from typing import *
# from math import ceil


# 첫번쨰거울에서 시작 , (방향,위치,튕긴거울수) - whle문 돌려,
N = int(input())
graph = [list(input()) for _ in range(N)]
sx, sy, isend = 0, 0, False
for i in range(N):
    for j in range(N):
        if graph[i][j] == "#":
            sx, sy = i, j
            isend = True
            break
    if isend:
        break
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
q = [(0, sx, sy, 0), (0, sx, sy, 1), (0, sx, sy, 2),
     (0, sx, sy, 3)]  # 튕긴 거울의 수|좌표|현재 나가는 방향


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < N


# 빈공간 - 계속 , 벽,out of range - stop, 거울 - 양갈래로 직진 큐 생성
# 무한 루프를 도는 빛이 있으므로 최단거리로 이동을 살펴야한다.
while q:
    w, x, y, di = q.pop(0)
    while True:  # 빛의 이동
        nx, ny = x+dx[di], y+dy[di]
        if not inRange(nx, ny):
            break
        if graph[nx][ny] == "*":
            break
        if graph[nx][ny] == "#":
            # print(f"END : {nx,ny,w,di}")
            if not(nx == sx and ny == sy):
                print(w)
                exit(0)
        if graph[nx][ny] == "!":
            q.append((w+1, nx, ny, (di+1) % 4))
            q.append((w+1, nx, ny, (di-1) % 4))
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
#.!*.*.*.
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

"""
