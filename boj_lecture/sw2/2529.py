from math import factorial
import sys
from collections import deque
import math

sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()


def isgood(a: int, b: str, c: int):
    if b == '<':
        return a < c
    else:
        return a > c

# 현재까지 데이터 상테에서, good검사를 해서, 넣어본다.


def go(ndata: []):
    global AnsList
    # print(ndata)
    # ndata를 다 모은경우는 K+1 길이가 됨
    if len(ndata) == K+1:
        tmp = "".join(map(lambda e: str(e), ndata))
        AnsList.append(tmp)
        return
    # ndata길이가 0 이면 그냥 무조건 처음 넣어
    for i in range(10):
        L = len(ndata)
        if L == 0 or isgood(ndata[-1], Blist[L-1], i):
            if check[i]:
                continue
            ndata.append(i)
            check[i] = True
            go(ndata)
            ndata.pop()
            check[i] = False
    # ndata 길이가 1이상이면 이제 비교를 하면서 넣어


check = [False]*(10)
AnsList = []
K = int(input())
Blist = input().split()

data = []
go(data)
AnsList.sort()
print(AnsList[-1])
print(AnsList[0])
