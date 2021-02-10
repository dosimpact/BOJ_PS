import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, S = map(int, input().split())
data = list(map(int, input().split()))
ANS = 0

# 크기가 양수인 부분수열


def go(n: int, p: int):  # 현재까지 고른 배열, 고를 배열 idx
    # p가 끝점이면 합체크
    if p == len(data):
        if n == S:
            global ANS
            ANS += 1
        return
    # 선택 o ,x
    go(n+data[p], p+1)
    go(n, p+1)  # 다 안고르는 경우
    return


go(0, 0)
if S == 0:
    print(ANS-1)
else:
    print(ANS)

"""
5 0
-7 -3 -2 5 8

5 1
-7 -3 -2 5 8

1 1
1

1 0
1

"""
