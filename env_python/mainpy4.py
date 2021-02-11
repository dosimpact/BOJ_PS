import re
import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


t = int(sys.stdin.readline().rstrip())
regex = re.compile('(100+1+|01)+')
for _ in range(t):
    print('YES' if regex.fullmatch(sys.stdin.readline().rstrip()) else 'NO')
