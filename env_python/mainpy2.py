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

    ansMax = max(span, ansMax)

    check_alpha[graph[x][y]] = True
    check[x][y] = True
    #  for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        DFS(nx, ny, span+1)
    check[x][y] = False
    check_alpha[graph[x][y]] = False

<< << << < HEAD

DFS(0, 0, 1)
print(ansMax)
"""
❌ 다른답
3 6
HFDFFB
AJHGDH
DGAGEH
>❌ 4
>6

❌ 시간 초과
- check_alpha 배열로
- basecase는 함수 스택에 최대한 안쌓이도록 최적화
- 더 줄일려면 메모지에이션..?

2 4
CAAB
ADCB
>3

2 4
AAAB
ADCB
>1

2 4
ABCD
HGFE
>5

1 1
A
>1

4 4
AAAH
BAAG
CDEF
AAAF
>8
=======
"""

>>>>>> > 7bfffbf4e25e7e4d2d2bcec6f88b45072b8caae1
"""
