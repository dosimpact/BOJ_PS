import sys


sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P = P[::-1]

d = [0 for _ in range(N)]
d[0] = P[0]

for i in range(1, N):
    d[i] = P[i]
    # 탐색  0 ~ i-1 까지
    for j in range(0, i):
        if P[j] < P[i]:
            d[i] = max(d[i], d[j] + P[i])
print(max(d))
