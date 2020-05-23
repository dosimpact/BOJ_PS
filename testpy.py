

import sys
from collections import deque
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()


data = 1789
setData = set(list(str(data)))

print(setData)
print(len(setData))
