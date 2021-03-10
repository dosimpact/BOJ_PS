from sys import exit, maxsize
from collections import deque


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

check_fire = [[maxsize for _ in range(C)] for _ in range(R)]
check_psn = [[maxsize for _ in range(C)] for _ in range(R)]
psn = [(i, j) for i in range(R) for j in range(C) if graph[i][j] == "J"]
fires = [(i, j) for i in range(R) for j in range(C) if graph[i][j] == "F"]

# 불먼저 이동, 지훈이동
# 불의위치-벽 이동 불가 , 지훈이동 - 벽,불차오른것 이동 불가

dq = deque()
for x, y in fires:
    check_fire[x][y] = 0
    dq.append((x, y))

while dq:
    x, y = dq.popleft()
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        if not(nx >= 0 and ny >= 0 and nx < R and ny < C):
            continue
        if graph[nx][ny] == "#":
            continue
        if check_fire[nx][ny] != maxsize:
            continue
        check_fire[nx][ny] = check_fire[x][y]+1
        dq.append((nx, ny))
dq = deque()
for x, y in psn:
    check_psn[x][y] = 0
    dq.append((x, y))
while dq:
    x, y = dq.popleft()
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        if not (nx >= 0 and ny >= 0 and nx < R and ny < C):
            print(check_psn[x][y]+1)
            exit(0)
        if graph[nx][ny] == "#":
            continue
        if check_psn[nx][ny] != maxsize:
            continue
        if check_psn[x][y]+1 >= check_fire[nx][ny]:
            continue
        check_psn[nx][ny] = check_psn[x][y]+1
        dq.append((nx, ny))
print("IMPOSSIBLE")
"""
4 4
####
#JF#
#..#
#..#
>3

4 4
####
#JF#
#.F#
#..#
>IMPOSSIBLE


4 4
####
#J.#
#..#
#F.#
>IMPOSSIBLE


4 5
.....
####F
#J.#F
...#.
>❌ IMPOSSIBLE 불이 지나가지 못한 자리를 0으로 하면 사람이 못 지나갑니다.
>2
"""
