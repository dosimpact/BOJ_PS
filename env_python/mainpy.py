import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

s = input().rstrip()
if len(s) % 2 == 0:  # 10
    f = s[:len(s)//2]  # 5
    b = s[len(s)//2:]  # 5
else:
    # 11
    f = s[:len(s)//2]  # 5
    b = s[(len(s)//2)+1:]  # 5

b = b[::-1]
for k in range(len(f)):
    if f[k] != b[k]:
        print(0)
        sys.exit(0)

print(1)
