
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    A.append(int(input()))
for _ in range(M):
    B.append(int(input()))

res = [0 for _ in range(len(A))]

for Be in B:
    for idx, Ae in enumerate(A):
        if Ae <= Be:
            res[idx] += 1
            break
print(res.index(max(res))+1)

"""
5 3 1 4

4 3 2

"""
