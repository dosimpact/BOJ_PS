"""

https://www.acmicpc.net/problem/2231
"""


import math
import sys


def input(): return sys.stdin.readline().rstrip()


X, Y = map(int, input().split())

Z = int((Y/X)*100)

# Z+1 이 목표

dZ = (((Y+1)/(X+1))*100) - (((Y)/(X))*100)
#print("->", X, Y, Z, dZ)
a = dZ

if Z != 99 and round(a, 9) != 0:
    # 가능성
    print(math.ceil(1/a))
else:
    print(-1)
