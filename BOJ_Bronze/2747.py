import sys


input = sys.stdin.readline


N = int(input())
LIMIT_N = 50
memo = [-1 for _ in range(LIMIT_N)]


def dp(x: int):
    # baseCase
    if x <= 1:
        return x
    # memoCase
    if memo[x] != -1:
        return memo[x]
    # top-down Case
    memo[x] = dp(x-1) + dp(x-2)
    return memo[x]


print(dp(N))
