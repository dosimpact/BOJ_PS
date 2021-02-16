import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

print("".join(list(map(lambda x: x[0], input().rstrip().split("-")))))
