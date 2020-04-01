"""


"""

import sys


def input(): return sys.stdin.readline().rstrip()


t = int(input())

for _ in range(t):
    n = int(input())
    csum, gsum = 0.0, 0.0
    for _ in range(n):
        a, b = map(float, input().split())
        csum += a
        gsum += (b*a)
    print(int(csum), round(gsum/csum, 1))
