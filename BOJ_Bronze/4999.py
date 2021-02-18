import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

p = input().strip()
pa = p.count("a")
t = input().strip()
ta = t.count("a")
print("no") if pa < ta else print("go")
