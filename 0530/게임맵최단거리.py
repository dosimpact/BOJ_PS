
import sys


def input(): return sys.stdin.readline().rstrip()


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


def bfs(x: int, y: int):
    global check
    check[x][y] = 1
    q = [(x, y)]
    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if inRange(nx, ny) and graph[nx][ny] == 1 and check[nx][ny] == 0:
                # print(
                #     f"check[nx][ny] = check[x][y] + 1:{check[nx][ny]} = {check[x][y]} + 1")
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))


graph = None
check = None
N, M = None, None  # 가로 세로,
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(maps):
    global graph, check, N, M
    answer = 0
    graph = maps
    N = len(graph)
    M = len(graph[0])
    check = [[0 for _ in range(M)] for _ in range(N)]
    # -----init-----
    bfs(0, 0)
    for row in check:
        print(*row)
    if check[N-1][M-1] == 0:
        return -1
    else:
        return check[N-1][M-1]


solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
         1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]	)
