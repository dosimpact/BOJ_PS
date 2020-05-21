import sys
import math


def input(): return sys.stdin.readline().rstrip()

"""
2 // T
6 12 10 // H W N
30 50 72 // H W N
"""

a, b, v = map(int, input().split())

tmpans = (v-a)/(a-b)
tmpans = math.ceil(tmpans)
print((tmpans+1))
