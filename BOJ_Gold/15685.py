import sys


def input(): return sys.stdin.readline()


def rc(d: int):
    d = d+1
    return d if d <= 3 else 0


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = [[0 for _ in range(101)] for _ in range(101)]  # 100 100 짜리 격자,

N = int(input())

for _ in range(N):
    (y, x, d, g) = map(int, input().split())
    #print(x, y, d, g)
    dlist = []
    dlist.append(d)
    for i in range(g):  # 1세대면 1번 놀아나볼까
        n = list(map(lambda x: rc(x), dlist))
        n.reverse()
        dlist.extend(n)
    # print(dlist)
    board[x][y] = 1
    for dl in dlist:
        x = x + dx[dl]
        y = y + dy[dl]
        if x >= 0 and x <= 100 and y >= 0 and y <= 100:
            board[x][y] = 1

# TMP = 10
# for i in range(TMP):
#     for j in range(TMP):
#         print(board[i][j], end=" ")
#     print()

ANS = 0
for i in range(101):
    for j in range(101):
        if(board[i][j] == 1 and i + 1 <= 100 and j + 1 <= 100):
            if board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
                ANS += 1
print(ANS)
