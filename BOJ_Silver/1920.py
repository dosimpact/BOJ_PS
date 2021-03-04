import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
want = list(map(int, input().split()))


def BSearch(arr: List[int], left: int, right: int, target: int):
    if left > right:
        return -1
    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return BSearch(arr, mid+1, right, target)
    else:
        return BSearch(arr, left, mid-1, target)


for w in want:
    res = BSearch(data, 0, len(data)-1, w)
    if res == -1:
        print(0)
    else:
        print(1)
