import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

N, M = map(int, input().split())  # 나무 갯수와, 나무 길이
trees = list(map(int, input().split()))
trees.sort()
left, right = 0, max(trees)  # 커팅하는 제일 작은 높이(조건ok최적X),커팅 최고높이(조건X,최적o)


def check(cutting: int):
    take = 0
    for tree in trees:
        if tree >= cutting:
            take += (tree - cutting)
    return take >= M


while True:
    if left+1 >= right:
        break
    mid = (left+right)//2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
"""
4 7
20 15 10 17

- 예외 케이스 - 안가져가도 되는 경우
4 0
20 15 10 17

- endpoint - 1인경우
4 1
20 15 10 20
>19

- endpoint - MAX 인경우
4 10
1 2 3 4
>0

- 예외 케이스 - 다 잘라도 못가져가는 경우
4 500
20 15 10 17
"""
