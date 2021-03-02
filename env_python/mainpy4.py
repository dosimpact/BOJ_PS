import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 붐버맨
# RC 직사각형 격자, 비거나 폭탄
# 폭탄 : 3초 폭팔 - 폭탄 + 인접4칸 빈칸 - 연쇄반응 없다.
# 일부칸 폭탄 설치 - 1초 아무것도 안함 - 1초 폭탄없는곳에 다 설치 - 1초 3초전에 설치한 폭탄 펑

# 2차원 배열 - 폭탄 or 빈캄
# 덱 - 폭탄 터지는 시간
#

"""
6 7 3 # 격자판 로 , 컬럼, N초 상한선
.......
...O...
....O..
.......
OO.....
OO.....
"""
