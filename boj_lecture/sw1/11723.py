# https://www.acmicpc.net/problem/11723

import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


M = int(input())
S = 0

for _ in range(M):
    com = input().split()
    if com[0] == "add":  # 추가 , OR 로
        x = int(com[1])
        S = S | (1 << x)
    if com[0] == "remove":  # 제거, AND + NOT
        x = int(com[1])
        S = S & ~(1 << x)
    if com[0] == "check":  # exits,  AND
        x = int(com[1])
        res = S & (1 << x)
        print(1) if res else print(0)
    if com[0] == "toggle":  # XOR 연산자 이용
        x = int(com[1])
        S = S ^ (1 << x)
    if com[0] == "all":  # 1~20 = 0~20까지로 가정 , 21개 , N =21
        # S = S | (2**20 - 1)
        S = S | ((1 << 21) - 1)
    if com[0] == "empty":
        S = 0
    # print(f"S : {S} {bin(S)}")
