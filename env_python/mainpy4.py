

import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**6)

Debug = False

res = 0

people = []

memoW = []
memoB = []
heapq.heapify(memoW)
heapq.heapify(memoB)


def tryonBlack():
    pass


def tryonWhite():
    pass


for data in sys.stdin:
    people.append(map(int, data.split()))

for person in data:
    if person[0] >= person[1]:
        tryonWhite(person[0])
        tryonBlack(person[1])
    else:
        try
"""
di 처리 :
 1. di-1 의 상태를 저장 , 두개의 최소힙큐로, 뺀앞의 사람이 곧 짤릴사람임
 2. pi의 취직시도, > 구조 조정

"""
