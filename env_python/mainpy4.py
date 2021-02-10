import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())  # 7일, =>
T: List[int] = []
P: List[int] = []

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

maxVal = 0


def go(day: int, earn: int):  # 현재 날짜, 벌어들인 수익
    global maxVal
    if day == N:  # 퇴사 날짜보다 길어진 경우 , = 상담할것이 없는경우
        maxVal = max(earn, maxVal)
        return
    if day > N:
        return
    go(day+T[day], earn+P[day])  # 더 상담이 가능한 경우 - 할래, 안할래
    go(day+1, earn)


go(0, 0)
print(maxVal)
