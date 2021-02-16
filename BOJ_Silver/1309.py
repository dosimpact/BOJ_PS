import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
D = [[0 for _ in range(3)] for _ in range(N)]  # [N번집][R,g,b] 최소값
D[0][0], D[0][1], D[0][2] = 1, 1, 1
DIVER = 9901
for i in range(1, N):
    D[i][0] = D[i-1][0] + D[i-1][1]+D[i-1][2]
    D[i][1] = D[i-1][0] + D[i-1][2]
    D[i][2] = D[i-1][0] + D[i-1][1]
    D[i][0], D[i][1], D[i][2] = D[i][0] % DIVER, D[i][1] % DIVER, D[i][2] % DIVER
print(sum(D[N-1]) % DIVER)
