import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# M 단독 스킬, 연계 스킬
# 연계스킬은 , 다른 스킬을 사용한 후 가능
# 근접 공격, 염력, 불 뿜기, 물 뿌리기, 회복
# 근접 > 염력,불 뿜기
# 염력 >  회복 또는 물 뿌리기
# DFS + BF

ansTmp = []


def DFS(now: str):

    return


def main():
    skills = input().split()
    N = int(input())
    graph = {}
    for _ in range(N):
        u, v = (input().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    # 시작점을 어떻게 잡아야할지
    print(graph)
    check = dict()
    for sk in skills:
        check[sk] = False
    for key in graph.keys():
        check[key] = True
        DFS(key)
        check[key] = False
    return


if __name__ == "__main__":
    main()

"""
h g f w r
4
h g
h f
g r
g w

h g r
h g w
h f

"""

# 연속 스킬 단독 스킬 여부 check 했어야 한다.
# 의존성 있는 스킬 : g,f,r,w => 유일 시작점 h
# 시작점 여러개인거 있나?
