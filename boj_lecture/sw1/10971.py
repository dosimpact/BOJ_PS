

import sys
from itertools import permutations, combinations

Debug = False


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()

"""
https://www.acmicpc.net/problem/10971
"""

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# 방문할 노드는 0 1,2,3 > 1,2,3 순열

trcs = [i for i in range(1, n)]
trcs = list(permutations(trcs))

ansMin = -1
for trc in trcs:

    isposs = True
    ansTmp = 0

    if graph[0][trc[0]] != 0:
        ansTmp += graph[0][trc[0]]
    else:
        isposs = False

    for i in range(len(trc)-1):  # 1 2 3
        if graph[trc[i]][trc[i+1]] != 0 and isposs:  # 0 1 | 1 2 | 2 3
            ansTmp += graph[trc[i]][trc[i+1]]
        else:
            isposs = False
    if graph[trc[-1]][0] != 0 and isposs:
        ansTmp += graph[trc[-1]][0]
        if ansMin == -1 or ansMin > ansTmp:
            ansMin = ansTmp

        # 끝

        # 실제로 방문해보고 결과값을 구한다.
print(ansMin)
