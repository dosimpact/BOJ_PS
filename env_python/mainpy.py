# import sys
# import math
# from typing import *
# import itertools

# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


def node(val: int, cnt: int):
    # 초과인 경우
    if val > B:
        return
    # 찾은 경우
    if val == B:
        print(cnt+1)
        exit(0)
        return
    # 계속인 경우 1. 제곱을 해본다. 2 자리수를 늘려본다.
    for i in range(1, 30):
        node(val*(2 ** i), cnt+1)
    for i in range(1, 10):
        node(int(str(val) + "1"*i), cnt+1)
    return


A, B = map(int, input().split())
node(A, 0)
print(-1)
