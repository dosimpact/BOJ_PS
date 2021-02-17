import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

A = input().strip()
B = input().strip()
D = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]  # [0,0] 계열 사용 X

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:  # 같은 경우
            D[i+1][j+1] = D[i][j]+1
            continue
        else:  # 다른 경우
            D[i+1][j+1] = max(D[i+1][j], D[i][j+1])

print(D[len(A)][len(B)])
