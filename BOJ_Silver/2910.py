import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N, C = map(int, input().split())
data = list(map(int, input().split()))
ddict = dict()
ddict_period = dict()
cnt = 1
for d in data:
    if d in ddict:
        ddict[d] += 1
    else:
        ddict[d] = 1
        ddict_period[d] = cnt
        cnt += 1

data.sort(key=lambda x: (ddict[x], -ddict_period[x]), reverse=True)
print(*data)

"""
5 2
2 1 2 1 2

6 2
1 2 1 2 1 2


6 2
2 1 2 1 2 1 
"""
