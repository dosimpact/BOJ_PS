from sys import stdin, setrecursionlimit
from itertools import combinations
from collections import deque

for dx, dy in combinations(zip([0, 0, -1, 1], [-1, 1, 0, 0]), 2):
    print(dx, dy)
