import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


data = dict()
allcnt = 0
while True:
    t = input().strip()
    if t == "":
        break
    allcnt += 1
    if t in data:
        data[t] += 1
    else:
        data[t] = 1

parsedData = []
for key in data:
    parsedData.append([key, (data[key]/allcnt)*100])
parsedData.sort(key=lambda x: x[0])

for d in parsedData:
    print("%s %.4f" % (d[0], d[1]))
