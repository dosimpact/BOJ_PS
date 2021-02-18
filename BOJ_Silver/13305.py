import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())

idx = [i for i in range(N-1)]
road = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]


sortedIdx = list(sorted(idx, key=lambda x: price[x]))

ans = 0
maxLeftPoint = len(price)
for i in range(len(sortedIdx)):
    cpointer = sortedIdx[i]  # 1 , 1번째 가장싼 가격으로 1번째 도로부터 다 연료를 넣으면 됨
    if cpointer < maxLeftPoint:
        ans += (sum(road[cpointer:maxLeftPoint])*price[cpointer])
        maxLeftPoint = cpointer  # 1
    if maxLeftPoint == 0:
        break
print(ans)
