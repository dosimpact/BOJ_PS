"""

재귀로 푼다. 방향성을 가지고

"""

import sys
DEBUG = False


def input(): return sys.stdin.readline().rstrip()


def go(x: int, y: int, dr: int):
    # fb) 체크를 두번해주었네. 혜자여
    #check[i][j] += 1
    # 다음 탐색뱡향
    for ndr in [0, 1, 2, 3]:
        if ndr == (dr+2) % 4:
            continue
        nx, ny = (x+dx[ndr], y+dy[ndr])
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if graph[nx][ny] == '.' and check[nx][ny] <= 1:
                check[nx][ny] += 1
                go(nx, ny, ndr)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if graph[i][j] == '.' and check[i][j] == 0:
            # fb)한번 시작을 했으면, 끝 -> 왜냐 u턴을 안하고 다 돌수 있는지 판단하는것이기 때문!
            check[i][j] += 1
            go(i, j, 1)
            break
if DEBUG:
    print(graph)
    print(check)

for i in range(n):
    for j in range(m):
        if check[i][j] == 1:
            print(1)
            exit(0)
print(0)
"""


"""
