import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


# 2x2x2 큐브
# 1,2....24 큐브 > 색상 1...6 까지
# 6면체마다, 시계방향 반시계 방향 돌릴 수 있다. - 아니다.
# x,y,z 축 마다 시계,반시계 - 6 케이스
# 1. 발상 - 12개 경우 다 매핑?
# 2.
