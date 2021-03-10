import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil
from functools import reduce


input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

ans = sys.maxsize


def go(idx: int, a, b):
    global ans
    if idx == N:
        if not a and not b:
            return
        ans = min(abs(reduce(lambda x, y: x*y, a) - sum(b)), ans)
        return

    #  골라봐 안골라봐
    a.append(data[idx][0])
    b.append(data[idx][1])
    go(idx+1, a, b)
    a.pop()
    b.pop()
    go(idx+1, a, b)


a = deque()
b = deque()
go(0, a, b)
print(ans)
