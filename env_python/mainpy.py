import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
memo = [-1]*(12)

memo[1] = 1
memo[2] = 2
memo[3] = 4

# dp [i] =  dp[i-1] + dp[i-2] + dp[i-3]

for i in range(4, 11):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

for _ in range(N):
    a = int(input())
    print(memo[a])
