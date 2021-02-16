import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
d = [False for _ in range(N+10)]

d[1], d[2], d[3], d[4] = True, False, True, True

for i in range(5, N+1):
    if d[i-1] and d[i-3] and d[i-4]:
        d[i] = False
    else:
        d[i] = True

print("SK") if d[N] else print("CY")
