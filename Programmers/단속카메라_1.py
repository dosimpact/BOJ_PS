
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


SIZE = 60000 + 1
pivot = 30000


check = []
meta = [0]*SIZE


def solution(routes):
    global check, meta

    for i in range(len(routes)):
        for j in range(2):
            routes[i][j] += pivot
    check = [False] * len(routes)
    ans = 0

    for [sidx, eidx] in routes:
        for i in range(sidx, eidx):
            meta[i] += 1

    while check.count(False) > 0:
        pos = meta.index(max(meta))
        ans += 1
        for i, [sidx, eidx] in enumerate(routes):
            if check[i] == False and sidx <= pos and pos <= eidx:
                for idx in range(sidx, eidx):
                    meta[idx] -= 1
                check[i] = True
    print(check)

    return ans


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
