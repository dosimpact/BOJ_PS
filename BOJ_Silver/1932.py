import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]  # [0][0]
D = [[0 for _ in range(i+1)] for i in range(N)]
D[0][0] = data[0][0]

for i in range(1, N):  # 1층부터
    # 0 ,1 가능
    for j in range(0, i+1):  # i층의 j번째 노드
        left, right = 0, 0
        if j != 0:
            left = D[i-1][j-1]
        if j != i:
            right = D[i-1][j]
        D[i][j] = max(left, right) + data[i][j]
print(max(D[N-1]))
