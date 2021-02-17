import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

ss = input().strip()
data = []
pos = []

while ss:
    if ss[0] == '+':
        pos.append(True)
        ss = ss[1:]
        tmp = ""
        while ss and ss[0].isnumeric():
            tmp += ss[0]
            ss = ss[1:]
        data.append(tmp)
    elif ss[0] == '-':
        pos.append(False)
        ss = ss[1:]
        tmp = ""
        while ss and ss[0].isnumeric():
            tmp += ss[0]
            ss = ss[1:]
        data.append(tmp)
    else:
        pos.append(True)
        tmp = ""
        while ss and ss[0].isnumeric():
            tmp += ss[0]
            ss = ss[1:]
        data.append(tmp)
low = 0
while low < len(data) and pos[low]:
    low += 1
ans = 0
for i in range(0, low):
    ans += int(data[i])
for i in range(low, len(data)):
    ans = ans - int(data[i])

print(ans)

"""
55-50+40
"""
