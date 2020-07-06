

import sys


def input(): return sys.stdin.readline().rstrip()


N = float(input())
rnd = -1
e = 1
while True:
    if N < 10:
        break
    # 96
    if N > (10**e):
        N = round(N+0.1, rnd)
        e += 1
        rnd -= 1
    else:
        break
print(int(N))
