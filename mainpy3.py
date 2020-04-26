

import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()


L, P = map(int, input().split())
data = list(map(int, input().split()))

su = L*P
for d in data:
    print(d-su, end=" ")
