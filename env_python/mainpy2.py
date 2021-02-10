import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


L, C = map(int, input().split())
data = list(input().split())
data.sort()

# n를 만들었다, p를 고를차례


def isVaild(s: str):
    # 자 2개 이상, 모 1개 이상
    mo = 0
    ja = 0
    for ch in s:
        if ch in list("aeiou"):
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2


def go(n: str, p: int):  # L까지 만들어봐
    # 더이상 고를것이 없다, or  완성해봄
    if len(n) == L:
        # print("tmp", n)
        if isVaild(n):
            print(n)
        return
    if p >= C:
        return
    go(n+data[p], p+1)
    go(n, p+1)
    return


go("", 0)
