"""


"""

import sys


def input(): return sys.stdin.readline().rstrip()


a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
    print(sum(a))
elif sum(a) == sum(b):
    print(sum(a))
else:
    print(sum(b))
