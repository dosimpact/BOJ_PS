
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
Diver = 1000000000
N = int(input())


d = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        if j + 1 <= 9:
            d[i][j] += d[i-1][j+1]
        if j - 1 >= 0:
            d[i][j] += d[i-1][j-1]
        d[i][j] = d[i][j] % Diver
print(sum(d[N]) % Diver)
