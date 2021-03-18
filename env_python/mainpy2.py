import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 데스나이트 6곳 규칙에 의해 이동
# NN 체스판, 두칸 , start > end 이동 최소 횟수
# 0,0 행 열 시작, 밖 이동 불가

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

# 그냥 BFS?
check = [[0 for _ in range(N)] for _ in range(N)]
dq = deque()
check[r1][c1] = 1
dq.append((r1, c1))

while dq:
    x, y = dq.popleft()
    if x == r2 and y == c2:
        break
    for dx, dy in zip([-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if check[nx][ny] != 0:
            continue
        check[nx][ny] = check[x][y] + 1
        dq.append((nx, ny))


if check[r2][c2] == 0:
    print(-1)
else:
    print(check[r2][c2] - 1)


"""

"""
