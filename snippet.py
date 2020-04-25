

import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


Debug = False
checkU = None
checkR = None
SIZE = 11

# 현재 고른 시간안에 모든 사람 n 명을 다 검사 할 수 있느냥

d = {
    'U': [0, 1],
    'D': [0, -1],
    'R': [1, 0],
    'L': [-1, 0],
}


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < SIZE and y < SIZE


def makeCheck(x: int, y: int, di: str):  # 현재 위치에서 가는 방향
    if di == 'U':
        checkR[x][y] = 1
    elif di == 'D':
        checkR[x][y-1] = 1
    elif di == 'R':
        checkU[x][y] = 1
    elif di == "L":
        checkU[x-1][y] = 1


def solution(dirs):
    global checkR, checkU
    checkU = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    checkR = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    # -------------------------
    x, y = 5, 5
    for di in dirs:
        # 현재 위치에서 이동하고 ( 가능하다면 )
        nx, ny = x + d[di][0], y + d[di][1]
        if inRange(nx, ny):
            makeCheck(x, y, di)
            x, y = nx, ny
            # check를 추가해준다.
    res = 0
    for C in checkU:
        res += C.count(1)
    for C in checkR:
        res += C.count(1)
    return res


print(solution("ULURRDLLU"))
