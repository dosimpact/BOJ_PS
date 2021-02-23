import sys
import math
import re
import heapq
from collections import deque
from typing import *
import copy
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

# 차변 변경 불가 > 추월 불가
# 숨거진 조건 - 1차선

N = int(input())
iCars = [input().strip() for _ in range(N)]
oCars = [input().strip() for _ in range(N)]
forwardCars = []
cnt = 0
# 정상적인 경우
while oCars:
    # 이미 나감 처리된 차
    if iCars[0] in forwardCars:
        iCars.pop(0)
        continue
    if iCars[0] == oCars[0]:
        iCars.pop(0), oCars.pop(0)
    else:
        cnt += 1
        forwardCars.append(oCars.pop(0))
print(cnt)

"""
4
a
b
c
d
d
a
b
c

4
a
b
c
d
d
a
c
b

4
a
b
c
d
b
c
d
a

4
a
b
c
d
c
a
d
b
"""
