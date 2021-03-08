import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

# BOJ 거리
# #전부 다 살피는 경우 # min 사용

N = int(input())
board = input().strip()  # 0~N-1 방문
d = [math.inf for _ in range(N)]
d[0] = 0
for i in range(1, N):
    for j in range(0, i):
        isSkip = False
        if board[i] == 'B' and board[j] != 'J':
            isSkip = True
        if board[i] == 'O' and board[j] != 'B':
            isSkip = True
        if board[i] == 'J' and board[j] != 'O':
            isSkip = True
        if isSkip:
            continue
        d[i] = min(d[i], d[j]+(i-j)**2)

if d[-1] == math.inf:
    print(-1)
else:
    print(d[-1])
