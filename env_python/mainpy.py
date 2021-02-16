import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
data = list(map(int, input().split()))

d = [0 for _ in range(N)]

for i in range(len(data)):
    d[i] = data[i]
    for j in range(0, i):
        if data[j] < data[i]:
            d[i] = max(d[j]+data[i], d[i])

print(max(d))
