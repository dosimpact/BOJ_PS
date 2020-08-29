import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 1ST 그래프 입력
N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
MAX_VAL = sum([i*2+1 for i in range(D+1)])+sum([i*2+1 for i in range(D)])


def inRange(x, y):
    return x >= 0 and y >= 0 and x < N and y < N


def BFS(startX, startY):
    check = [[-1 for _ in range(N)] for _ in range(N)]
    check[startX][startY] = 0
    count = 1
    q = [(startX, startY)]
    while q:
        x, y = q.pop(0)
        if check[x][y] >= D:
            continue
        for k in range(4):
            nx, ny = x+dx[k], y + dy[k]
            if inRange(nx, ny) and graph[nx][ny] == 0 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y] + 1
                count += 1
                q += [(nx, ny)]
    return count


ansMAX = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            res = BFS(i, j)
            ansMAX = max(ansMAX, res)
        if ansMAX == MAX_VAL:
            print(ansMAX)
            exit(0)
print(ansMAX)

# 2ST 모든 물 부분에 돌을 던져본다.
