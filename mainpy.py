import sys


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
data = [0]*(n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for it in range(i, j+1):
        data[it] = k

print(' '.join(map(str, data[1:])))
