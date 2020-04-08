import sys


def input(): return sys.stdin.readline()


"""
이렇게 풀면 안되

해당 위치에서 5개  > -> 위로 아래로 다 내려가봐야되, 그래서 총 5개가 되어야함.
20*20*8
"""


def inRange(i, j):
    return (i >= 0 and j >= 0 and i < L and j < L)


def check(i, j, board):

    for di in [[(1, 0)(-1, 0)], [(0, 1), (0, -1)], [(-1, -1), (1, 1)], [(1, -1), (-1, 1)]]:
        pass

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    # 해당 지점에서 8곳을 끝까지 돌면서, 딱 5개면 정답
    for k in range(8):
        if board[i][j] != 0:
            color = board[i][j]
            cnt = 1
            x, y = i+dx[k], j+dy[k]
            while inRange(x, y):
                if color == board[x][y]:
                    cnt += 1
                    x, y = x+dx[k], y+dy[k]
                else:
                    break
            if cnt == 5:
                return board[i][j]
    return 0


L = 19

board = [list(map(int, input().split())) for _ in range(L)]

for i in range(L):
    for j in range(L):
        res = check(i, j, board)
        if res == 1 or res == 2:
            print(res)
            print(i+1, j+1)
            exit(0)
        else:
            continue
print(0)
"""

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

"""
