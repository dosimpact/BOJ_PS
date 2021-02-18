import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


T = int(input())
for i in range(T):
    data = dict()
    case = int(input())
    for _ in range(case):
        val, key = input().split()
        if key not in data:
            data[key] = 1
        else:
            data[key] += 1
    ans = 1
    for key in data:
        ans = ans * (data[key] + 1)
    print(ans - 1)

"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""