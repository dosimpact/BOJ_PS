import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])
