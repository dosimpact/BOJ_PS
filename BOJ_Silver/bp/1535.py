import sys
import heapq
import re
import math
from collections import deque, defaultdict
from typing import *
from math import ceil, factorial
from itertools import combinations


sys.setrecursionlimit(10**6)
# N명, 얻는경우 안얻는경우,재귀

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

ans = 0


def go(idx: int, HP: int, Joy: int):
    global ans
    if HP <= 0:
        return
    if idx == N:
        ans = max(ans, Joy)
        return
    go(idx+1, HP, Joy)
    go(idx+1, HP - L[idx], Joy+J[idx])


go(0, 100, 0)
print(ans)
