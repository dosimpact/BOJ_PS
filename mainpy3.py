

import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
data = list(map(int, input().split()))

a, b = divmod(n-1, k-1)
if b != 0:
    a += 1
print(a)
