import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

data = input().strip()

wanted = "UCPC___"
p = 0
while data:
    if data[0] == wanted[p]:
        p += 1
    data = data[1:]
print("I love UCPC") if p == 4 else print("I hate UCPC")
