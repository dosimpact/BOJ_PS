import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


T = int(input())
for i in range(T):
    isEndWith_1 = False
    isPtn = True
    ss: str = input().strip()
    ss = ss+"E"
    while not ss.startswith("E"):
        # print("ss:", ss, " ", len(ss))
        # 01
        if ss.startswith("01"):  # 01 제거
            ss = ss[2:]
            isEndWith_1 = False
        # 100+1+
        elif ss.startswith("100") or (ss.startswith("00") and isEndWith_1):  # 100 제거

            if isEndWith_1:
                ss = ss[2:]
            else:
                ss = ss[3:]
            isEndWith_1 = False

            while ss[0] == "0":  # 0+제거
                ss = ss[1:]
            if (not ss) or ss[0] != "1":
                isPtn = False
                break
            if ss[0] == "1":
                ss = ss[1:]
            while ss[0] == "1":
                ss = ss[1:]
                isEndWith_1 = True
        else:
            isPtn = False
            break
    if isPtn:
        print("YES")
    else:
        print("NO")
