import sys
import heapq
import re
import math
from collections import deque, defaultdict
from typing import *
from math import ceil, factorial
from itertools import combinations

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


# 투포인터 풀이
# 병합정렬의 merge 부분임
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
APtr, BPtr = 0, 0  # 넣을 예정

while APtr < len(A) and BPtr < len(B):
    if A[APtr] < B[BPtr]:
        ans.append(A[APtr])
        APtr += 1
    else:
        ans.append(B[BPtr])
        BPtr += 1

# 남은 A,B 넣기
while APtr < len(A):
    ans.append(A[APtr])
    APtr += 1
while BPtr < len(B):
    ans.append(B[BPtr])
    BPtr += 1

print(*ans)
