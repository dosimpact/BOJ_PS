import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

D = dict()
A = input().strip()
B = input().strip()
if len(A) > len(B):
    B, A = A, B

for i in range(1, len(A)):
    # 길이가 i 인 문자열에서 공통인 부분 찾기
    for j in range(0, len(A)):
        res = B.find(A[j])
        if res != -1:
            if i not in D:
                D[i] = []
            D[i].append([A[j+1:], B[res+1:]])
    break


ans = 0
for i in range(2, len(A)):
    D[i] = []  # 길이 2를 만들어야함
    # 길이 3을 만들면 1을 지워도 된
    if i >= 3:
        del(D[i-2])
    DDown = D[i-1]
    for pair in DDown:
        a, b = pair
        if (not a)or (not b):
            continue
        for j in range(0, len(a)):  # i-1 부터 검색
            res = b.find(a[j])
            if res != -1:
                D[i].append([a[j+1:], b[res+1:]])
                ans = i
print(ans)

"""
AWOFNOWEFNOEWNFEWONFEWOFNAOEWFONEWFNOANAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWG
NAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWGNAWGNWENGNGNWEGNWEGNEGWENGNEGNGNWEGNWENGENWG
"""
