

import sys


def input(): return sys.stdin.readline().rstrip()


Debug = False


"""
2
10
15

3
2
15
10
"""

N = int(input())
rop = [int(input()) for _ in range(N)]
rop.sort(reverse=True)

if Debug:
    print(rop)

ansMax = 0

for idx, r in enumerate(rop):
    su = idx+1
    ansMax = max(su*r, ansMax)

print(ansMax)
