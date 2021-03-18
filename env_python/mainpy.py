
import sys
import functools
from typing import *

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
data = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))
data.sort()


def BSearch(L: int, R: int, target: int):
    if L > R:
        return -1
    mid = (L+R)//2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return BSearch(mid+1, R, target)
    else:
        return BSearch(L, mid-1, target)


for q in query:
    res = BSearch(0, len(data)-1, q)
    if res == -1:
        print(0)
    else:
        print(1)
