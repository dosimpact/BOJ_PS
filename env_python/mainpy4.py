import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


# X1 .. Xn
# 공유기 C개,집에 설치함
# 1. 가장 인접한 공유기 사이 거리,
# 2. 그 거리를 최대로
# 1 2 4 8 9
# 1,2,4 > 1,2 > 가장 인접 1 =>  최대로
# 1 4 9 > 3,5 >가장 인접 3 => 최대임
# BF - 공유기 랜덤 설치 불가능
# N개중 C개를 뽑는것 - 각 거리가 나옴 - 최대
# 이분 탐색인가?
# 1 2 3
# 처음과 마지막은 무조건 고른다.
# 중간에 집 후보들을 살피면서, 인접한 두 집의 거리의차가 가장 작은 녀석으로 골라나간다.

"""
5 3
1
2
8
4
9
"""
