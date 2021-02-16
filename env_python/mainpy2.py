import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

data = list(map(int, input().split()))

for i in range(len(data)-1):
    if data[i] > data[i+1]:
        print("Bad")
        sys.exit(0)

print("Good")
