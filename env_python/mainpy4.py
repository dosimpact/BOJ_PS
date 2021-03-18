import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


# 원숭이는 K번만 나이트 움직인다. 그외는 인접한 칸으로 이동(4방향)
# 최단거리이동 = BFS
# 0 <= K <= 30,
# check[200][200][30] = 12 * 10 ** 5 = 1.2 * 10**6 = KB
# BFS 이동 + 노드가 분리되는 경우

K = int(input())
K += 1
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
check = [[[0 for _ in range(K)] for _ in range(C)] for _ in range(R)]
dq = deque()
check[0][0][0] = 1
dq.append((0, 0, 0))

while dq:
    x, y, k = dq.popleft()
    # 일반 이동하는 경우
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        if not((0 <= nx < R) and (0 <= ny < C)):
            continue
        if check[nx][ny][k] != 0:
            continue
        if graph[nx][ny] == 1:
            continue
        check[nx][ny][k] = check[x][y][k]+1
        dq.append((nx, ny, k))
    # 말처럼 이동하는 경우
    for dx, dy in zip([-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]):
        nx, ny, nk = x+dx, y+dy, k+1
        if not((0 <= nx < R) and (0 <= ny < C)):
            continue
        if nk >= K:
            continue
        if check[nx][ny][nk] != 0:
            continue
        if graph[nx][ny] == 1:
            continue
        check[nx][ny][nk] = check[x][y][k]+1
        dq.append((nx, ny, nk))

res = [check[R-1][C-1][i] for i in range(K) if check[R-1][C-1][i] != 0]

# print(res)
# for r in check:
#     print(r)


if not res:
    print(-1)
else:
    print(min(res)-1)


"""
0
4 4
0 1 0 0
1 0 0 0
0 0 1 0
0 1 0 0
>6 ❌ 조건 빼먹음
>-1

1
4 4
0 1 0 0
1 0 1 0
0 1 0 0
0 0 0 0
>1 ❌ 조건 빼먹음
>-1

1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
>4

1
4 4
0 1 0 0
1 0 0 0
0 0 1 0
0 1 0 0
>4

10
3 2
0 0
0 0
0 0
>1



1
4 4
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
>-1

2
4 4
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
>2
"""
