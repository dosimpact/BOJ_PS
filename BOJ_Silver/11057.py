import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


n = int(input())

d = [[0 for _ in range(0, 10)] for _ in range(0, n + 1)]
for i in range(0, 10):
    d[1][i] = 1

for i in range(2, n + 1):  # i번째 오르막 수
    for j in range(0, 10):  # i길이 오르막수 중, j로 끝나는거 채우자.
        for k in range(0, j + 1):
            d[i][j] = (d[i][j] + d[i - 1][k]) % 10007

print(sum(d[n]) % 10007)
