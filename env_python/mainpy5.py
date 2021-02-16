import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
data = list(map(int, input().split()))
data.reverse()
d = [0 for _ in range(N+1)]  # d: i를 포함하는 가장긴+증가하는 부분 수열 **길이**
dList = [[] for _ in range(N+1)]

for i in range(len(data)):
    dList[i] = [data[i]]
    d[i] = 1  # 3  # 기본값 새로만드는 경우
    for j in range(0, i):  # 이어가는 경우 아닌경우  # 0,1,2
        if data[j] < data[i] and d[i] < d[j]+1:
            d[i] = d[j]+1
            dList[i] = dList[j] + [data[i]]

maxAns = max(d)
maxIdx = d.index(maxAns)
print(maxAns)
print(*dList[maxIdx])
