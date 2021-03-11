import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil
from itertools import combinations

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


d = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def go(a: int, b: int, c: int):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return go(20, 20, 20)
    if d[a][b][c] != -1:
        return d[a][b][c]

    if a < b and b < c:
        d[a][b][c] = go(a, b, c-1)+go(a, b-1, c-1)-go(a, b-1, c)
        return d[a][b][c]
    else:
        d[a][b][c] = go(a-1, b, c) + go(a-1, b-1, c) + \
            go(a-1, b, c-1) - go(a-1, b-1, c-1)
        return d[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {go(a, b, c)}")
