import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 토지개발
# 가로로 N개 연결된 토지, N은 2지수승
# 토지 개발 > 이익
# 절반을 나눠 한쪽 개발 , 그중 max 값이 이익
# 1칸 남으면 땡


def main():
    N = int(input())
    data = list(map(int, input().split()))
    ans = 0
    while len(data) >= 2:
        u, v = data[:len(data)//2], data[len(data)//2:]
        uMax, vMax = max(u), max(v)
        if uMax > vMax:
            ans += uMax
            data = v
        else:
            ans += vMax
            data = v
    print(ans)
    return


if __name__ == "__main__":
    main()

"""
8
1 3 10 9 6 2 3 2
>19

2
1 99
>99
"""
