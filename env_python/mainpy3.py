import sys
from typing import *
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

sneak = deque()
N = int(input())
K = int(input())
borad = [[0 for _ in range(N + 2)] for _ in range(N + 2)]  # 1 벽, 2 사과
for _ in range(K):
    x, y = map(int, input().split())
    borad[x][y] = 2

L = int(input())
moves = []
for _ in range(L):
    t, c = input().split()
    moves.append((int(t), c))
moves.sort(key=lambda x: x[0])


for i in range(N + 2):
    for j in range(N + 2):
        if i == 0 or j == 0 or j == N + 1 or i == N + 1:
            borad[i][j] = 1
time = 0
sneak.append((1, 1))  # 0 이 앞 , -1 꼬리
di = 1  # 0,1,2,3
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def isCollision(x: int, y: int):
    if x == 0 or y == 0 or x == N + 1 or y == N + 1:  # 벽 = inrange
        # print(f"벽충돌")
        return True
    if (x, y) in sneak:
        # print(f"self 충돌")
        return True
    return False


while True:
    # print(f"time:{time} di:{di} sneak: {sneak}")
    # 몸늘려 - 사과 체크 - 그대로 or 줄어들어 - 회전 체크
    nx, ny = sneak[0][0] + dx[di], sneak[0][1] + dy[di]
    if isCollision(nx, ny):
        print(time + 1)
        sys.exit(0)
    sneak.appendleft((nx, ny))
    if borad[nx][ny] == 2:
        borad[nx][ny] = 0  # 사과 냠냠
    else:
        sneak.pop()
    time += 1
    if moves and moves[0][0] <= time:
        t, d = moves.pop(0)
        if d == "D":
            di = (di + 1) % 4
        else:
            di = (di - 1) % 4

    # 게임 종료 -  벽 또는 자기자신의 몸과 부딪
