"""
https://www.acmicpc.net/problem/13699

t(n)=t(0)*t(n-1)+t(1)*t(n-2)+...+t(n-1)*t(0)
"""

import sys

sys.setrecursionlimit(10**6)
memo = {}


def go(t: int):
    if t == 0:
        return 1
    if t in memo:
        return memo[t]
    tmp = 0
    for i in range(t):
        j = t - 1 - i
        tmp += go(i)*go(j)
    memo[t] = tmp
    return memo[t]


n = int(input())
print(go(n))

# 0 1
# 0 1  1 0
# 0 2  1 1  2 0
