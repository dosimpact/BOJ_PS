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