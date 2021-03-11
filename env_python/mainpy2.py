import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

# 자두 나무
# 풀이법 - dfs 트리를 돈다.
# 풀이법 - dp 설계를 한다. - 메모리가 걱정 ? -3*1000


T, E = map(int, input().split())  # 자두 갯수, 에너지 제한
P = []
for _ in range(T):
    P.append(int(input()) - 1)
d = [[[0 for _ in range(2)] for _ in range(E + 1)] for _ in range(T)]
# 자두 ,에너지, 위치,

# 현재 위치에 자두가 있는경우
# - 가만이 있어서 자두 먹는경우, 움직여서 먹는경우
# 현재 위치에 자두가 없다.
# - 없지만 존버하는 경우, 없지만 움직여서 존버하는 경우
# 3번, 1번위치, 에너지가 5,4,3,2,1


# d[자두번호][에너지][위치]
# 자두 떨어지는 위치
# d[자두번호][에너지][위치] = d[자두번호-1][0~에너지][위치] +1 , d[자두번호-1][0~에너지-1][다른위치] +1 ,

# d[자두번호][에너지][위치] = d[자두번호-1][0~에너지][위치] , d[자두번호-1][0~에너지-1][다른위치],

for e in E + 1:
    d[0][e][P[0]] = 1


print("hello world")