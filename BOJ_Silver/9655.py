import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())

print("CY") if T % 2 == 0 else print("SK")
