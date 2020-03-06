import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

"""
fb1)
2의 n승은 20 까지
n팩은 10까지
이렇게 재귀 3분할이면 3의 n승인데, n이 100 이여, 시간초과 날수밖에

fb2)
어려운 dp 맞다. 외자.

d[i] = max

d[i-1] - 1
d[i-3] *2 ( j = 1 )
d[i-4] *3

d[i - (j+2)] * (j+1) ( 1 <= j <= i-3)
....

"""

d = {}

N = int(input())

d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
for i in range(2, N+1):
    d[i] = d[i-1] + 1
    for j in range(1, i-2):
        if d[i] < d[i - (j+2)]*(j+1):
            d[i] = d[i - (j+2)]*(j+1)

print(d[N])
