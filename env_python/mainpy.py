from collections import deque


# K번만 말처럼 이동가능, (장애물 통과 가능)
# 노드가 분리되는 경우, 원숭이 동작의 최솟값
K = int(input())
M, N = map(int, input().split())

# K=1   만해도, 0번 말처럼, 1번 말처럼 2가지 경우
graph = [list(map(int, input().split())) for _ in range(N)]
dist = [[[0 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]  # [x][y][k]


dq = deque()
dist[0][0][0] = 1
dq.append((0, 0, 0))


def inRange(x: int, y: int):
    return 0 <= x < N and 0 <= y < M


while dq:
    x, y, w = dq.popleft()
    # k += 1
    for dx, dy in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
        nx, ny = x + dx, y + dy
        if not inRange(nx, ny):
            continue
        if w + 1 > K:
            continue
        if graph[nx][ny] == 1:
            continue
        if dist[nx][ny][w + 1] != 0:
            continue
        dist[nx][ny][w + 1] = dist[x][y][w] + 1
        dq.append((nx, ny, w + 1))
    # k += 0
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x + dx, y + dy
        if not inRange(nx, ny):
            continue
        if graph[nx][ny] == 1:
            continue
        if dist[nx][ny][w] != 0:
            continue
        dist[nx][ny][w] = dist[x][y][w] + 1
        dq.append((nx, ny, w))


res = [e for e in dist[N - 1][M - 1] if e != 0]

if len(res) == 0:
    print(-1)
else:
    print(min(res) - 1)

"""
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0


1
4 4
0 1 0 0
1 0 0 0
0 0 1 0
0 1 0 0
>4

1
2 2
0 0
0 0 
>2
"""