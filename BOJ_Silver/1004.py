import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())


def isIn(x: int, y: int, cx: int, cy: int, r: int):
    dist = (x-cx)**2+(y-cy)**2
    return dist < r**2


for _ in range(T):
    my = []
    there = []
    start_x, start_y, end_x, end_y = map(int, input().split())
    n = int(input())
    for i in range(n):
        cx, cy, r = map(int, input().split())
        if isIn(start_x, start_y, cx, cy, r):
            my.append(i)
        if isIn(end_x, end_y, cx, cy, r):
            there.append(i)
    print(len(set(my) | set(there)) - len(set(my) & set(there)))
