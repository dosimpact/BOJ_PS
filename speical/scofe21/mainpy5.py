import sys
import math
from collections import deque
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 시선 이동, N,M 인 화면 정보
# c 시선 시작 가능 지점, x 비선호 콘텐츠 , .선호 콘텐츠
# 최하단 이동 경로 -  아래 ,좌,우 3가지 탐색
# 기준 경로 = 좌우로 가장 적게 이동한 경로


M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

start_points = [(i, j) for i in range(N)
                for j in range(M) if graph[i][j] == 'c']
ans_min = math.inf


def BFS(sx: int, sy: int):
    global ans_min
    check = [[-1 for _ in range(M)] for _ in range(N)]
    dq = deque()
    check[sx][sy] = 0
    dq.append((sx, sy))

    while dq:
        x, y = dq.popleft()
        for i, (dx, dy) in enumerate(zip([1, 0, 0], [0, -1, 1])):
            # if i ==0 인경우 내려가는 경우임 그외 좌우
            nx, ny = x+dx, y+dy
            # 범위 - 실패 | 범위 - 성공 | x 체크 |
            if (nx >= N):
                ans_min = min(ans_min, check[x][y])
                continue
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if graph[nx][ny] == 'x':
                continue
            if check[nx][ny] != -1:
                continue
            if i == 0:  # 내려가는 경우임 - 무조건 확장
                check[nx][ny] = check[x][y]
                dq.appendleft((nx, ny))
            else:  # 좌우 이동하는 경우
                check[nx][ny] = check[x][y] + 1
                dq.append((nx, ny))
    # for r in check:
        # print(*r)
    return


for sx, sy in start_points:
    # print(f"sx, sy {sx, sy}")
    BFS(sx, sy)
    # print(f"ansmin {ans_min}")


if ans_min == math.inf:
    print(-1)
else:
    print(ans_min)

"""
4 5
c.xc
....
xx..
...x
x..x
"""
