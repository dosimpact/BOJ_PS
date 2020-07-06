# https://www.acmicpc.net/problem/1261
import sys


def input(): return sys.stdin.readline().rstrip()


"""
알고스팟 : 다음으로 이동하는데 가중치가 다른 경우 => 0,1 덱사용
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    global graph, check
    check[x][y][z] = 0
    dq = []
    dq.append((x, y, z))
    while len(dq) != 0:
        (nowx, nowy, nowz) = dq.pop(0)
        for k in range(4):
            nx = nowx + dx[k]
            ny = nowy + dy[k]
            if (nx >= 0 and ny >= 0 and nx < N and ny < M) and (graph[nx][ny] == 0) and (check[nx][ny][nowz] == -1):
                check[nx][ny][nowz] = check[nowx][nowy][nowz] + 1
                dq.append((nx, ny, nowz))
            elif (nx >= 0 and ny >= 0 and nx < N and ny < M) and (graph[nx][ny] == 1) and (check[nx][ny][nowz] == -1):
                if nowz == 1:
                    pass
                elif nowz == 0:
                    check[nx][ny][nowz+1] = check[nowx][nowy][nowz] + 1
                    dq.append((nx, ny, nowz+1))


"""
check[0] 벽을 한번도 안부수고 bfs 최단
check[1] 벽을 한번 부수고 bfs 최단

주변노드를 탐색 | 범위 체크 | 벽이 아닌경우 와 벽인경우 ||
벽이 아니라면 , 방문 체크를 하고 | 엔큐
벽이라면
"""

(N, M) = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
check = [[[-1 for _ in range(2)] for _ in range(M)] for _ in range(N)]

bfs(0, 0, 0)


a = check[N-1][M-1][0]
b = check[N-1][M-1][1]
if (a == b == -1):
    print(-1)
elif(a == -1):
    print(b+1)
elif(b == -1):
    print(a+1)
else:
    print(min(a, b)+1)
