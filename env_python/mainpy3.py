import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

data = input().strip()

print(
    data.count('a') +
    data.count('e') +
    data.count('i') +
    data.count('o') +
    data.count('u') 
)
