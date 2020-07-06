"""

https://www.acmicpc.net/problem/2231
"""


import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())

for k in range(1, n):
    now = k
    tmp = list(str(k))
    for e in tmp:
        now += int(e)
    if n == now:
        print(k)
        exit(0)
print(0)
