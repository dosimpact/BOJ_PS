import sys
from collections import deque


def input(): return sys.stdin.readline()


N = int(input())
i = 0
bol = [[it+1, int(e)] for it, e in enumerate(input().split())]


for _ in range(len(bol)):
    idx, val = bol.pop(i)
    print(idx, end=' ')
    if len(bol) == 0:
        break
    if val >= 0:
        i = (i+val-1) % len(bol)
    else:
        i = (i+val) % len(bol)
