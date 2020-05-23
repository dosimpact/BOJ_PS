

import sys
from collections import deque
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    rotSu = int(input())
    datas = []
    actions = []
    for _ in range(4):
        datas.append(deque(list(map(int, input().split()))))
    for _ in range(rotSu):
        u, v = map(int, input().split())
        actions.append((u, v))
    print(datas)
    print(actions)
