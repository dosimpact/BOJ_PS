import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

A = input().strip()
A = " " + A
B = input().strip()
B = " " + B
D = [[0 for _ in range(len(B))] for _ in range(len(A))]  # A > B

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            D[i][j] = D[i - 1][j - 1] + 1
        else:
            D[i][j] = max(D[i - 1][j], D[i][j - 1])
h, w = len(A) - 1, len(B) - 1
ans = ""
val = D[h][w]
while True:
    if h <= 0 or w <= 0 or D[h][w] == 0:  # 완전히 아무것도 안겹칠때 ( 0일때는 더이상공통인거 없으니 종료 )
        break
    while D[h][w] != 0 and D[h - 1][w] == val:
        h -= 1
    while D[h][w] != 0 and D[h][w - 1] == val:
        w -= 1
    if D[h][w] == D[h - 1][w - 1] + 1:
        ans += str(A[h])
        h -= 1
        w -= 1
        val = D[h][w]
print(D[len(A) - 1][len(B) - 1])
print(ans[::-1])
"""
ACAYKP
CAPCAK
"""