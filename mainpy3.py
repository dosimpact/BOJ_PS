import sys
import functools
from itertools import permutations, combinations


def input(): return sys.stdin.readline().rstrip()


Debug = True

"""


"""
n = int(input())
sus = list(map(int, input().split()))

for i in range(1, max(sus)+1):
    isposs = True
    for su in sus:
        if su % i == 0:
            pass
        else:
            isposs = False
    if isposs:
        print(i)
