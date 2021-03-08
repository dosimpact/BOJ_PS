import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# ( 한쪽팔길이 - 1 )* 4 - 1 = 너비

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def _inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


# 만들 수 없으면 false | len 이 넓이다.
def makeCross(x: int, y: int, L: int):
    res = []
    isposs = True
    for k in range(4):
        nx, ny = x + dx[k] * L, y + dy[k] * L
        if not _inRange(nx, ny) or graph[nx][ny] != "#":
            isposs = False
            break
        res.append((nx, ny))
    if not isposs:
        return False
    else:
        return res


# 겹치는지 여부
def interSections(cross1, cross2):
    return len(set(cross1) & set(cross2)) >= 1


# print(interSections([(1, 2), (1, 3)], [(1, 8), (1, 4)]))
ansMax = []
for x1 in range(N):
    for y1 in range(M):
        if graph[x1][y1] == ".":
            continue
        L1 = 0
        cross1 = [(x1, y1)]
        while True:
            for x2 in range(N):
                for y2 in range(M):
                    if graph[x2][y2] == ".":
                        continue
                    if x1 == x2 and y1 == y2:
                        continue
                    cross2 = [(x2, y2)]
                    L2 = 0
                    while True:
                        # print(
                        #     f"[] x1,y1,L1,x2,y2,L2,cross1,cross2 {x1,y1,L1,x2,y2,L2,cross1,cross2} "
                        # )
                        if not interSections(cross1, cross2):
                            ansMax.append(len(cross1) * len(cross2))
                        L2 += 1
                        tmp2 = makeCross(x2, y2, L2)
                        if not tmp2:
                            break
                        cross2 += tmp2

            # 길이를 늘려서 점검
            L1 += 1
            tmp1 = makeCross(x1, y1, L1)
            if not tmp1:
                break
            cross1 += tmp1
if ansMax:
    print(max(ansMax))
else:
    print(0)
"""
7 7
...#...
...#...
...#...
#######
...####
...#.#.
...#...
>25

7 7
...#...
...#...
...#...
#######
...###.
...#.#.
...#...

3 3
###
###
###
>5


3 3
.#.
###
.#.
>1

3 4
..#.
####
..#.
>5


2 2
..
..
>0

2 2
..
.#
>0

2 2
..
##
>1

2 2
##
##
>1
"""