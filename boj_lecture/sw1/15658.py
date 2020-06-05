

import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
Debug = False


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()


"""
"""


def go(now: int, ops: [], idx: int):
    global ansList
    # 다 만든 경우
    if idx >= len(datas):
        ansList.append(now)
        return
    # 못만든느 경우는 없다.

    # 4가지 돌자.
    if ops[0] > 0:
        go(now+datas[idx], [ops[0]-1, ops[1], ops[2], ops[3]], idx+1)
    if ops[1] > 0:
        go(now-datas[idx], [ops[0], ops[1]-1, ops[2], ops[3]], idx+1)
    if ops[2] > 0:
        go(now*datas[idx], [ops[0], ops[1], ops[2]-1, ops[3]], idx+1)
    if ops[3] > 0:
        tmp = 0
        if now < 0:
            now = -now
            tmp = now//datas[idx]
            tmp = -tmp
        else:
            tmp = now // datas[idx]
        go(tmp, [ops[0], ops[1], ops[2], ops[3]-1], idx+1)


Su = int(input())
datas = list(map(int, input().split()))
ops = list(map(int, input().split()))

ansList = []

go(datas[0], ops, 1)

print(max(ansList))
print(min(ansList))
