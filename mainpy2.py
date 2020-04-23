

import sys
from copy import deepcopy
from collections import defaultdict

sys.setrecursionlimit(10**8)


def input(): return sys.stdin.readline().rstrip()

"""
20
3
5 3
10 2
1 5
"""

T = int(input())
k = int(input())
cins = []
for _ in range(k):
    cins.append(list(map(int, input().split())))
cins.sort()

print(cins)

LEmts = list(zip(*cins))[0]
CEmts = list(zip(*cins))[1]

Lvar = [0] * len(LEmts)

while True:
    # 반복문 종료인지 검사
    print(Lvar)
    Lvar[0] += 1
    for i in range(len(Lvar)-1, -1, -1):
        if i == 0:
            if Lvar[i] >= LEmts[i]:
                break
        else:
            if LEmts[i] < Lvar[i]:
                Lvar[i] = 0
                Lvar[i+1] += 1
