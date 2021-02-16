import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
Cost = [list(map(int, input().split())) for _ in range(N)]  # [N번집][R,g,b] 비용
D = [[0 for _ in range(3)] for _ in range(N)]  # [N번집][R,g,b] 최소값
for i in range(3):
    D[0][i] = Cost[0][i]

for i in range(1, N):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + Cost[i][0]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + Cost[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + Cost[i][2]

print(min(D[N-1]))
