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

N, M = map(int, input().split())
data = list(map(int, input().split()))

ans, s, e, now = 0, 0, 0, 0
# s,e = 삭제할예정,더할예정
while True:
    if now == M:  # 답인경우 - 축소
        ans += 1
        now -= data[s]
        s += 1
        continue
    elif now > M:  # 큰경우 - 축소
        now -= data[s]
        s += 1
        continue
    else:  # 작은 경우 - 확대
        if e == N:  # 확대가 불가능한경우 - 끝! ( 전제 : 축소를 해볼만큼 해봄 ) = 마지막 분기위치
            break
        now += data[e]
        e += 1
print(ans)

"""
10 5
1 2 3 4 2 5 3 1 1 2
"""
