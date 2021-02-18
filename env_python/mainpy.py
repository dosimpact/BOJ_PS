import sys
import math
from typing import *

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


s = input().rstrip()
s = s + "E"
ans = 1
while not s.startswith("E"):
    if s[0] == "d":
        tmp = 10
        cnt = 0
        while s[0] == "d":  # 10,9,9,
            cnt += 1
            s = s[1:]
        if cnt > 1:
            tmp *= 9 ** (cnt - 1)
        ans *= tmp
    if s[0] == "c":
        tmp = 26
        cnt = 0
        while s[0] == "c":  # 10,9,9,
            cnt += 1
            s = s[1:]
        if cnt > 1:
            tmp *= 25 ** (cnt - 1)
        ans *= tmp
print(ans)