n = int(input())
dp = [n]*(n+1)
dp[0], dp[1] = 0, 1

for i in range(1, n+1):
    end = int(i**0.5)+1

    dp[i] = min((dp[i-j*j]+1) for j in range(1, end))
print(dp[n])
