import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline


N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()


def check(minDist: int):  # 이정돈 떨어져서 설치하면 ok
    # 첫번째 집은 설치
    lastHome = homes[0]
    cnt = 1
    for i in range(1, len(homes)):
        if homes[i] - lastHome >= minDist:
            cnt += 1
            lastHome = homes[i]
    return cnt >= C


ans = 0
left, right = 1, homes[-1]-homes[0]
while True:
    if left > right:
        break
    mid = (left+right)//2
    if check(mid):
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1

print(ans)
