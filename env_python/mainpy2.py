import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, S = map(int, input().split())
Arr = list(map(int, input().split()))
# 크기가 양수인 부분수열 , 공집합 제거
# 수열의 원소를 다 더한 값이 S
# 비트 마스크 풀이, 수열의 원소들은 이진수로 매핑된다.
ans = 0
for i in range(1, (1 << N), 1):  # 00000 (X),00001 , ... 11111
    # print(bin(i))
    sumT = 0
    for j in range(0, N):  # 1,2,...5
        if i & (1 << j):  # 존재성 > AND
            sumT += Arr[j]
    if sumT == S:
        ans += 1
print(ans)
