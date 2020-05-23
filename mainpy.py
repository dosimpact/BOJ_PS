

import sys
from collections import deque
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()


def solution(n):
    if n == 1:
        return 1
    L = len(str(bin(n))[2:])
    ans = 0
    for k in range(0, L+1):
        if n & 1 << k:
            ans += 3**(k)
    return ans


print(solution(10**10))
