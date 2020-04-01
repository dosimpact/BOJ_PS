

import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
Debug = False


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()

"""
https://www.acmicpc.net/problem/1759
"""


def isVaild(s: str):
    ja = 0
    mo = 0
    for e in s:
        if e == 'a' or e == 'e'or e == 'i'or e == 'o'or e == 'u':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(cur: str, idx: int):
    # 다 모은 경우 // baseCase 이므로 반드시 종료
    if len(cur) == L:
        if isVaild(cur):
            print(cur)
        return
    # 안되는 경우// baseCase 이므로 반드시 종료
    if idx >= len(datas):
        return
    # keep
    go(cur+datas[idx], idx+1)
    go(cur, idx+1)


L, C = map(int, input().split())
datas = input().split()
datas.sort()
go("", 0)
