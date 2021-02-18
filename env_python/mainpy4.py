import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N, P, Fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
taxi_x, taxi_y = map(lambda x: int(x) - 1, input().split())
clients = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(P)]
completed = [False for _ in range(P)]
remainClients = P
check = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(P)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < N


for i in range(P):  # i 번째 사람
    start_x, start_y, end_x, end_y = clients[i]
    check[i][start_x][start_y] = 0
    q = [(start_x, start_y)]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if inRange(nx, ny) and check[i][nx][ny] == -1 and graph[nx][ny] == 0:
                check[i][nx][ny] = check[i][x][y] + 1
                q.append((nx, ny))

for i in range(P):  # i 번째 사람
    for crow in check[i]:
        print(crow)
    print()
# 현재위치에서 가장 가까운 승객 태움, 행번호 우선,열번호 그다음
# 연료 리차지는 운송거리의 두배 , 운송중 바닥은 실패, 도착하자마자 바닥은 성공
# 남은 연료양 , 불가능하면 - 1
# 각 사람 BFS - 택시 - 사람 - 도착지 한번에 알 수 있음
# 현재 - 태워 - 도착 ** 반복

while remainClients > 0:
    # 1번고객,가는거리 3,도착거리 7, 도착위치 2,3
    who = -1
    go_dist_min = math.inf
    end_dist, end_x, end_y = 0, 0, 0
    for i in range(P):
        if completed[i]:
            continue
        go_dist_tmp = check[i][taxi_x][taxi_y]
        end_x_tmp, end_y_tmp = clients[i][2], clients[i][3]
        if go_dist_min > go_dist_tmp:
            go_dist_min = go_dist_tmp
            who = i
            end_dist = check[i][end_x_tmp][end_y_tmp]
            end_x, end_y = end_x_tmp, end_y_tmp

    completed[who] = True
    remainClients -= 1
    print(f"who : {who}")
    if Fuel < go_dist_min + end_dist:
        print(-1)
        sys.exit(0)
    Fuel -= go_dist_min + end_dist
    Fuel += (end_dist) * 2
    taxi_x, taxi_y = end_x, end_y
print(Fuel)
"""
6 3 15  , 6 6 격자, 3명 , 15 연료
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0 --- 격자
6 5 - 택시 위치
2 2 5 6 -- 승객 시작 끝
5 4 1 6
4 2 3 5 --- 
"""

# FB - -1로 아예 못가는 경우 예외
# FB - 고객 우선순위