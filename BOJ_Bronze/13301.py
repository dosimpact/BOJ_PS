import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
data = [0 for i in range(100)]
data[1] = 1
data[2] = 1
for i in range(3, N+3):
    data[i] = data[i-1]+data[i-2]
print(2*data[(N+2)])
