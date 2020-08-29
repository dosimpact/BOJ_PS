import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 그래프 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def inRange(x, y):
    return x >= 0 and y >= 0 and x < N and y < N
# 1ST 물을 이동시켜, 홍현이도 이동시켜서 - 벽을 세울 수 있는 곳의 후보들을 구해


checkW = [[-1 for _ in range(N)] for _ in range(N)]
checkH = [[-1 for _ in range(N)] for _ in range(N)]

# 물이동
checkW[0][0] = 0
q = [(0, 0)]
while q:
    nowX, nowY = q.pop(0)
    for k in range(4):  # 주변 노드를 탐색한다.
        nx, ny = nowX + dx[k], nowY + dy[k]
        if inRange(nx, ny) and graph[nx][ny] == 0 and checkW[nx][ny] == -1:
            checkW[nx][ny] = checkW[nowX][nowY] + 1
            q += [(nx, ny)]
# 홍현이동
checkH[N-1][N-1] = 0
q = [(N-1, N-1)]
while q:
    nowX, nowY = q.pop(0)
    for k in range(4):  # 주변 노드를 탐색한다.
        nx, ny = nowX + dx[k], nowY + dy[k]
        if inRange(nx, ny) and checkH[nx][ny] == -1:
            checkH[nx][ny] = checkH[nowX][nowY] + 1
            q += [(nx, ny)]
# print(checkW)
# print(checkH)
wallList = []
for i in range(N):
    for j in range(N):
        if checkW[i][j] == -1:
            continue
        if i == N-1 and j == N-1:
            continue
        if i == 0 and j == 0:
            continue
        if checkW[i][j] > checkH[i][j]:
            wallList.append((i, j))
# print(wallList)
# 2ST 후보들에 벽을 세워보며, MAX 값을 찾아낸다.
ansMAX = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0 and checkW[i][j] == -1:
            ansMAX += 1

# 후보에 벽을 세우고, BFS 을 돌려서 물을 채워본다. 그리고 빈공간의 갯수를 구해
for case in wallList:
    count = 0
    wx, wy = case
    graph[wx][wy] = 1
    # start
    checkW = [[-1 for _ in range(N)] for _ in range(N)]
    checkW[0][0] = 0
    q = [(0, 0)]
    while q:
        nowX, nowY = q.pop(0)
        for k in range(4):  # 주변 노드를 탐색한다.
            nx, ny = nowX + dx[k], nowY + dy[k]
            if inRange(nx, ny) and graph[nx][ny] == 0 and checkW[nx][ny] == -1:
                checkW[nx][ny] = checkW[nowX][nowY] + 1
                q += [(nx, ny)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and checkW[i][j] == -1:
                count += 1

    # end
    ansMAX = max(count, ansMAX)
    graph[wx][wy] = 0
print(ansMAX)
