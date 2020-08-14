import sys
input = sys.stdin.readline

N = int(input())
d = [N]*(N+1)

d[0], d[1] = 0, 1

for i in range(2, N + 1):  # 9
    end = int(i ** 1 // 2) + 1
    d[i] = min(d[i-j*j]+1 for j in range(1, end))  # 1 2 3
print(d[N])
"""
-
d[1] = 1
for i in range(2, N+1):
    if int(i**0.5) ** 2 == i:
        print(i)
-
10승
"""

"""
n=int(input())
dp=[n]*(n+1)
dp[0], dp[1]=0,1

for i in range(1,n+1):
    end=int(i**0.5)+1
    
    dp[i]=min((dp[i-j*j]+1) for j in range(1, end))  
print(dp[n])
"""
