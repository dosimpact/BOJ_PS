
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()

"""

"""


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    poss = False
    for t in range(x, M*N, M):
        # print(f"후보 {t} : <{x},{t%N}>")  # 6 1
        dy = t % N
        if dy == y:
            print(t+1)
            poss = True
            break
    if not poss:
        print(-1)

"""
?) 아직도 의문인건, 분명 M,N의 카테시안 곱으로 존재할것 같은데..
"""
