import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 카드 2
# N장의 카드, 1~N번호로 구성
# 뺀위카드버려,
N = int(input())
dq = deque()
for _ in range(1, N+1):
    dq.append(_)

while len(dq) >= 2:
    dq.popleft()
    t = dq.popleft()
    dq.append(t)

print(dq[0])
