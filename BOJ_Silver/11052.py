import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
"""
5
10 9 8 7 6
"""

N = int(input())
P = list(map(int, input().split()))
P = [0] + P
memo = [0]*(N+1)
memo[1] = P[1]
for i in range(2, N+1):
    # i개를 팔래
    for j in range(0, i):
        memo[i] = max(memo[i], memo[j]+P[i-j])
print(memo[N])
