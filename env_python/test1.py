import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
# bottomup

dp = [0 for _ in range(0, 100)]
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])
