import sys
import math
from typing import *
import itertools
from collections import deque

N = int(input())
A = list(map(int, input().split()))
D = [[0 for _ in range(2)] for _ in range(N)]

D[0][0] = A[0]
D[0][1] = A[0]  # 0

for i in range(1, N):
    D[i][0] = max(D[i-1][0]+A[i], A[i])
    D[i][1] = max(D[i-1][0], D[i-1][1] + A[i])


res = D[0][0]
for e in D:
    res = max([res] + e)
print(res)
