import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
P = list(map(int, input().split()))
PR = P[::-1]

d = [0 for _ in range(N)]
d[0] = 1

dR = [0 for _ in range(N)]
dR[0] = 1


for i in range(1, N):
    d[i] = 1
    dR[i] = 1
    # 탐색  0 ~ i-1 까지
    for j in range(0, i):
        if P[j] < P[i]:
            d[i] = max(d[i], d[j] + 1)
        if PR[j] < PR[i]:
            dR[i] = max(dR[i], dR[j] + 1)
dR = dR[::-1]
# print(d)
# print(dR)
for i in range(len(d)):
    d[i] += dR[i]
print(max(d)-1)
