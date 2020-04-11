
import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


"""


"""
AList = []
BList = []

for _ in range(10):
    tmp = int(input())
    AList.append(tmp)
for _ in range(10):
    tmp = int(input())
    BList.append(tmp)

AList.sort(reverse=True)
BList.sort(reverse=True)

print(sum(AList[:3]), sum(BList[:3]))
