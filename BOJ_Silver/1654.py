import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

# N개의 랜선
# K개의 랜선 잘라
# 조건 : N 개 이상으로 만들 수 있냐
# left,right : 1단위로 잘라 , 최대 랜선의 길이로 잘라
K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
lines.sort()

left, right = 1, max(lines)


def check(cutUnit: int):
    cnt = 0
    for l in lines:
        cnt += l // cutUnit
    return cnt >= N


ans = 0
while True:
    if left > right:
        break
    mid = (left+right)//2
    if check(mid):  # 조건이 만족해, 요심내서 크게 잘라보자 > left 우상향
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1

print(ans)
"""
4 11
802
743
457
539
>200

2 20
10
10
>1

-end point
4 4
10
10
10
10
>10

"""
