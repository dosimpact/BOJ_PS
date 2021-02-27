import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 시간당 1천원
# h시간동안 p대의 PC 운영
price = None
MAX_H = None


def go(data: List[int], idx: int, time: int, whoPC: int):
    if time > MAX_H:  # 더볼 필요도 없다면
        return
    if idx == len(data):  # 끝까지 도달
        price[whoPC].append(time)
        return
    go(data, idx+1, time+data[idx], whoPC)
    go(data, idx+1, time, whoPC)
    return


def main():
    global price, MAX_H
    P, N, H = map(int, input().split())  # 피씨 수, 예약손놈, H까지
    data = [[] for _ in range(P+1)]
    # global var
    price = [[] for _ in range(P+1)]
    MAX_H = H
    for _ in range(N):
        u, v = map(int, input().split())
        data[u].append(v)
    for i in range(len(data)):
        data[i].sort()
    # 각 PC로 운영
    for p in range(1, P+1):
        go(data[p], 0, 0, p)
    for p in range(1, P+1):
        print(p, 1000*max(price[p]))


if __name__ == "__main__":
    main()

"""
1 3 5
1 3
1 4
1 5
>❌
1 5000

2 7 4
1 10
1 5
1 7
2 10
2 1
2 3
2 7
>
1 0
2 4000


1 3 7
1 3
1 4
1 5
>
1 7000
"""
