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

def main():
    N, M, E = map(int, input().split())  # 6개 땅콩중, 3개를 먹는다. 현재는 7위치다.
    data: List[int] = list(map(int, input().split()))
    left, right = E, E

    while M > 0:  # 남은 땅콩수  # 좌에서 가까운 땅콩은 ? 우에서 가까운 땅콩은?
        # left,right값을 추가해,
        data.extend([left, right])
        data = list(set(data))
        l_idx, r_idx = data.index(left), data.index(right)
        if l_idx > 0:
            l_idx -= 1
        if r_idx < len(data)-1:
            r_idx += 1
        l_len, r_len = abs(left-data[l_idx]), abs(right-data[r_idx])
        print(f"data{data}")
        data = list(filter(lambda x: x != left and x != right, data))
        # 해당 인덱스를 찾아 -1, +1 가능하면 해
        if l_len < r_len:  # 왼쪽 먹어
            left = data[l_idx]
        else:
            right = data[r_idx]

        M -= 1
    # 각 거리를 구해
    print(abs(left-right))
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
