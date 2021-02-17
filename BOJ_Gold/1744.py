import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()
mpoint = 0
while mpoint < len(data) and data[mpoint] <= 0:
    mpoint += 1

mArr = data[:mpoint]
pArr = data[mpoint:]
ans = 0
while mArr:
    if len(mArr) >= 2:
        ans += (mArr[0]*mArr[1])
        mArr = mArr[2:]
    elif len(mArr) == 1:
        ans += mArr[0]
        mArr = mArr[1:]
    else:
        print("Error")
pArr = pArr[::-1]
while pArr:
    if len(pArr) >= 2:
        if pArr[0] == 1 or pArr[1] == 1:
            ans += (pArr[0]+pArr[1])
        else:
            ans += (pArr[0]*pArr[1])
        pArr = pArr[2:]
    elif len(pArr) == 1:
        ans += pArr[0]
        pArr = pArr[1:]
    else:
        print("Error")
print(ans)
"""
4
-1
2
1
3

4
1
2
1
3

4
-1
-2
-1
-3

6
0
-1
-2
-3
4
5
"""
