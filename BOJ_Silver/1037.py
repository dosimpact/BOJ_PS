import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
An = list(map(int, input().split()))
An.sort()
print(An[0]*An[-1])
