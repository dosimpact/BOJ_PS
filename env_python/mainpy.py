from sys import setrecursionlimit, stdin
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 8)


# 유니온 파인드
N = int(input())  # 게이트 수
P = int(input())
plans = [int(input()) for _ in range(P)]
gate = [False for _ in range(N + 1)]
parents = [_ for _ in range(N + 1)]


def getP(x: int):
    if x == parents[x]:
        return x
    parents[x] = getP(parents[x])
    return parents[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px == py:
        return
    elif px > py:  # 5 3
        parents[px] = py
    else:
        parents[py] = px


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


ans = 0
prev = 0
gate[0] = True

for p in plans:
    isPoss = False
    for i in range(p, 0, -1):
        if gate[i]:
            continue
        union(prev, i)
        gate[i] = True
        prev = i
        ans += 1
        isPoss = True
        break
    if not isPoss:
        print(ans)
        exit(0)
print(ans)
