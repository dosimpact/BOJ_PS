

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
"""
2 #2번돌려
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1 #1번을 시계
3 -1 #3번을 반시계


1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
"""
