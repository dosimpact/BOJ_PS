

import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
Debug = False


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()

"""
https://www.acmicpc.net/problem/6603
"""


def go(b: [], idx: int, now: []):
    # fb) pass
    # 정답인 경우 bc
    if len(now) == 6:
        for e in now:
            print(e, end=" ")
        print()
        return
    # 가지 치기 bc
    # if idx >= len(now):
    if idx >= len(b):
        return

    now.append(b[idx])
    go(b, idx+1, now)
    now.pop()
    go(b, idx+1, now)
    # keep


while True:
    a, *b = map(int, input().split())
    if a == 0:
        exit(0)
    now = []
    go(b, 0, now)
    print()
