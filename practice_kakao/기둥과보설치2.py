import sys

Debug = False

# 특정 좌표에 기둥을 만들수 있는지

Gidong = []
Bow = []
N = 0


def inRange(x: int, y: int):
    return (x >= 0 and y >= 0 and x < N and y < N)


def canGidong(x: int, y: int):
    if y == 0:
        return True
    if inRange(x, y-1) and Gidong[x][y-1] == 1:
        return True
    if Bow[x][y] == 1:
        return True
    if inRange(x-1, y) and (Bow[x-1][y] == 1):
        return True
    return False
# 특정 좌표에 보를 만들 수 있는지


def canBow(x: int, y: int):
    if inRange(x, y-1) and Gidong[x][y-1] == 1:
        return True
    if inRange(x+1, y-1) and Gidong[x+1][y-1] == 1:
        return True
    if inRange(x-1, y) and inRange(x+1, y) and Bow[x-1][y] == 1 and Bow[x+1][y] == 1:
        return True
    return False

# (뭔가를 제거함) 특정 좌표의 기둥이 괜찮은지


def isOkGidong(x: int, y: int):
    if Gidong[x][y] == 1:
        return canGidong(x, y)
    else:
        return True

# (뭔가를 제거함) 특정 좌표의 보가 괜찮은지


def isOkBow(x: int, y: int):
    if Bow[x][y] == 1:
        return canBow(x, y)
    else:
        return True


def ConverRes():
    res = []
    n = len(Gidong)
    for i in range(n):
        for j in range(n):
            if Gidong[i][j] == 1:
                res.append([i, j, 0])
    for i in range(n):
        for j in range(n):
            if Bow[i][j] == 1:
                res.append([i, j, 1])
    res.sort(key=lambda x: (x[0], x[1], x[2]))
    return res


def solution(n, build_frame):
    global Gidong, Bow, N
    n += 1  # 5 6
    N = n  # 6
    Gidong = [[0 for _ in range(n)] for _ in range(n)]
    Bow = [[0 for _ in range(n)] for _ in range(n)]

    for (x, y, a, b) in build_frame:
        if b == 0:  # 삭제
            if a == 0:  # 기둥 > 위에 있는 기둥, 오른쪽 왼쪽에 있는 보 괜찮은지.
                Gidong[x][y] = 0
                if isOkGidong(x, y+1) and isOkBow(x, y+1) and isOkBow(x-1, y+1):
                    pass
                else:
                    if Debug:
                        print("D Reject", x, y, a, b)
                    Gidong[x][y] = 1
            if a == 1:  # 보 제거 > 양쪽 끝 보, 양쪽 끝 기둥
                Bow[x][y] = 0
                if isOkBow(x+1, y) and isOkBow(x-1, y) and isOkGidong(x, y) and isOkGidong(x+1, y):
                    pass
                else:
                    if Debug:
                        print("D Reject", x, y, a, b)
                    Bow[x][y] = 1
        elif b == 1:  # 생성
            if a == 0:  # 기둥
                if canGidong(x, y):
                    Gidong[x][y] = 1
                else:
                    if Debug:
                        print("C Reject", x, y, a, b,)
            elif a == 1:
                if canBow(x, y):
                    Bow[x][y] = 1
                else:
                    if Debug:
                        print("C Reject", x, y, a, b,)
    return ConverRes()


"""
단지 2차원 graph로 파싱을 함으로써,
n으로 풀 수 있다.

"""
