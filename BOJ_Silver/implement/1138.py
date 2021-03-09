import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil
from itertools import combinations

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
N = int(input())
data = list(map(int, input().split()))

# 1. 키가 큰 사람 부터 배치.
# 2. 현재까지 배치된 상황은 무조건 키큰 사람들, 그럼 나의 위치가 결정되어 있다.

res = []
for i in range(N-1, -1, -1):
    d = data[i]
    res.insert(d, i+1)
print(*res)

"""
4
2 1 1 0

4
0 2 1 0
>1 4 3 2
"""
