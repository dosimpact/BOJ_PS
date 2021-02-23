import sys
import math
import re
import heapq
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def solution(n: int):
    ans = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n // i
            if a == b:
                ans += a
            else:
                ans += a + b
    return ans


print(solution(5))
print(solution(12))
print(solution(16))