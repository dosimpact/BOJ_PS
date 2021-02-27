import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 땅콩 먹기
# N개의 땅콩 1차원 수직선위
# M개만 먹을 수 있다.
# 그리디 - 내 범위안에서 left,right 근접 땅따머기


# 땅콩을 체크 딕에 넣어
# left, right 증가 시키면서 멀어볼까?

# 첫 설계 잘못함

def main():
    N, M, E = map(int, input().split())  # 6개 땅콩중, 3개를 먹는다. 현재는 7위치다.
    data: List[int] = list(map(int, input().split()))
    left, right = E, E

    while M > 0:

        M -= 1
    return


if __name__ == "__main__":
    main()

"""
❌
6 3 0
2 4 5 8 11 12
> 11

6 3 7
2 4 5 8 11 12
>4
"""
