"""
https://www.acmicpc.net/problem/1660


 세 글자가 행, 열, 또는 대각선으로 연속할 때, 그 플레이어가 승리

"""

import sys

sys.setrecursionlimit(10**6)

n = int(input())

SIZE = 300001
dpSub = [0]*SIZE
dp = [0]*SIZE

dpSub[1] = 1
for i in range(2, SIZE):
    dpSub[i] = dpSub[i-1]+i

dp[1] = 1
for i in range(2, SIZE):
    dp[i] = dp[i-1] + dpSub[i]

# 사면체의 갯수다
ans = 0
while n > 0:
    for i in range(1, SIZE-1):
        if dp[i] <= n and n < dp[i+1]:
            n -= dp[i]
            ans += 1
            break
print(ans)
