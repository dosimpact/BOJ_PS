import sys
from collections import deque
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()


def isButy(year: int):
    setData = set(list(str(year)))
    return len(setData) == 4


def solution(p):
    p += 1
    while not isButy(p):
        p += 1
        pass
    return p
