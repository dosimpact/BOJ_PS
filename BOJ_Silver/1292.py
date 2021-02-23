import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

A, B = map(int, input().split())
M = max(A, B)
arr = []

j = 1
while M >= 0:
    arr.extend([j] * j)
    M -= j
    j += 1
print(sum(arr[A - 1 : B]))
