
import sys
import math
import functools
import itertools

DEBUG = False


sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()


s = 2
n = '1234567890'

s, n = input().split()
s = int(s)


graph = [[' ' for _ in range((s+2+1)*len(n))] for _ in range(2*s+3)]

if DEBUG:
    print(graph)

Num2Pos = {
    0: [0, 1, 2, 3, 4, 5],
    1: [1, 2],
    2: [0, 1, 3, 4, 6],
    3: [0, 1, 2, 3, 6],
    4: [1, 2, 5, 6],
    5: [0, 2, 3, 5, 6],
    6: [0, 2, 3, 4, 5, 6],
    7: [0, 1, 2],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6],
}


def Pos2Points(Pos: [], s: int):
    meta = {
        0: [(0, 1), (0, 1)],
        1: [(1, s+1), (1, 0)],
        2: [(s+2, s+1), (1, 0)],
        3: [(2*s+2, 1), (0, 1)],
        4: [(s+2, 0), (1, 0)],
        5: [(1, 0), (1, 0)],
        6: [(s+1, 1), (0, 1)],
    }

    def Adder(a: (), b: ()):
        return (a[0]+b[0], a[1] + b[1])

    res = []
    for p in Pos:
        [now, rel] = meta[p]
        res.append(now)
        for _ in range(s-1):  # p =0
            res.append(Adder(res[-1], rel))
    return res


for i, ne in enumerate(n):
    x, y = 0, 0+((s+3)*i)
    checks = Pos2Points(Num2Pos[int(ne)], s)
    for (dx, dy) in checks:
        nx, ny = x+dx, y+dy
        if nx == 0 or nx == s+1 or nx == 2*s+2:
            graph[nx][ny] = "-"
        else:
            graph[nx][ny] = "|"
# 출력하기
for row in graph:
    for e in row:
        print(e, end="")
    print()
