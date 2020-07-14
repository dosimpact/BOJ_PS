import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
checkW = [[-1 for _ in range(M)] for _ in range(N)]
checkG = [[-1 for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


def BFS_water():
    global checkW
    q = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '*':
                q.append((i, j,))
                checkW[i][j] = 0
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x+dx[k], y + dy[k]
            # 범위, 방문여부, 지도 체크
            if not inRange(nx, ny):
                continue
            if graph[nx][ny] == "X" or graph[nx][ny] == "D":
                continue
            if checkW[nx][ny] == -1:
                checkW[nx][ny] = checkW[x][y]+1
                q.append((nx, ny,))
# 그 다음에 고슴도치를 이동시켜서 checkG 를 채운다.


def BFS_go():
    global checkG
    q = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                q.append((i, j,))
                checkG[i][j] = 0
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x+dx[k], y + dy[k]
            if not inRange(nx, ny):
                continue
            if graph[nx][ny] == "*" or graph[nx][ny] == "X":
                continue
            # 가려고 하는곳에, 물이 찰수 있고, 아직 안찬경우
            # if (checkW[nx][ny] != -1 and checkW[nx][ny] <= checkG[x][y]+1):
                # continue
            # 가려고 하는곳이, 굴이 아니고, 물이 아직 안차거나 못가는 경우
            if graph[nx][ny] != 'D' and checkW[nx][ny] <= checkG[x][y]+1:
                continue
            # 물떄문에 가는지 못가는지 점검 -> -1이라는 물도 못가는데, 가는곳 바위 ?
            if checkG[nx][ny] == -1:
                checkG[nx][ny] = checkG[x][y]+1
                q.append((nx, ny,))


BFS_water()
BFS_go()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'D':
            if checkG[i][j] != -1:
                print(checkG[i][j])
            else:
                print("KAKTUS")
