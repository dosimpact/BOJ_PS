import sys
import heapq
import re
import math
from collections import deque, defaultdict
from typing import *
from math import ceil, factorial
from itertools import combinations

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


# 블라인드된 곳은 2**26 번 - 블라인드 전후로 swap 구하기

K = int(input())
N = int(input())
frontData = [chr(i + ord('A')) for i in range(K)]
backData = list(input().strip())
graph = []
bRow = 0
for _ in range(N):
    row = input()
    if row[0] == "?":
        bRow = _
    graph.append(row)


def goLadder(myRow, ladders):
    for ladder in ladders:
        for i in range(len(ladder)):
            if ladder[i] == "-":
                myRow[i], myRow[i+1] = myRow[i+1], myRow[i]


frontLadders = graph[:bRow]
blindLadder = graph[bRow:bRow+1]
backLadders = graph[bRow+1:]
goLadder(frontData, frontLadders)
goLadder(backData, backLadders[::-1])

delay = False
ans = ""
for i in range(len(frontData)-1):
    if delay:
        ans += "*"
        delay = False
        continue
    if frontData[i] == backData[i]:
        ans += "*"
    else:
        if frontData[i] != backData[i+1]:
            print("x"*(K-1))
            sys.exit(0)
        if not delay:
            ans += "-"
            delay = True
print(ans)

"""
10
5
HCGBEDJFIA
*-***-***
-*-******
?????????
-**-***-*
**-*-*-*-
"""
