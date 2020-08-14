
import sys
input = sys.stdin.readline


N = int(input())
d = [0] * (31)
d[0] = 1
d[1] = 0
d[2] = d[0]*3
d[3] = 0
d[4] = d[2]*3 + d[0]*2
for i in range(5, N + 1):
    if (i % 2 == 1):
        d[i] = 0
        continue
    d[i] = d[i-2]*3
    for j in range(i - 4, -1, -2):
        d[i] += (d[j] * 2)
print(d[N])
