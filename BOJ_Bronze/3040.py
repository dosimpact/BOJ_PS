import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

data = []
sumdata = 0
for i in range(9):
    t = int(input())
    sumdata += t  # //t += sumdata
    data.append(t)

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if 100 == sumdata - (data[i] + data[j]):
            for k in range(9):
                if k == i or k == j:
                    continue
                print(data[k])
            break
