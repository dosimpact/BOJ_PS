import math
import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
Debug = True


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()


"""
신뢰하는 관계 = 그래프

BFS 각각 돌리니까, NN+NM 시간복잡도, 10초 나온다.

BFS 에 메모지 도입하니, 순환하는 구조에서는 못 사용.

fb) 비어있는 set인 경우는 set() 라고 파이썬이 출력한다.

{1: set(), 3: set(), 4: {4}, 5: {5}}

"""

d = {}  # 1를 해킹하면, 1,2,3 을 해킹하는거나 마찬가지.


def dp(n: int):

    if n in d:  # 메모가 있는경우
        return d[n]

    # 내가 말단 노드인 경우
    if len(graph[n]) == 0:  # [[], [3], [3], [4, 5], [], []]
        d[n] = {n}
        return d[n]
    # 아닌 경우
    d[n] = {n}
    for e in graph[n]:
        d[n] = (d[n]) | (dp(e))
    return d[n]


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)  # b를 해킹하면 a는 덤

maxCnt = 0
for i in range(1, N+1):  # dp로 다 돌려볼꺼임.
    dp(i)
    maxCnt = max(maxCnt, len(d[i]))

ansTmp = []
for i in range(1, N+1):
    if len(d[i]) == maxCnt:
        ansTmp.append(i)
ansTmp.sort()
for ans in ansTmp:
    print(ans, end=" ")
