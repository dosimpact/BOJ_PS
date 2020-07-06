
import sys
import math
import functools
import itertools

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


obj = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    0: "E"
}
for _ in range(3):
    now = list(map(int, input().split()))
    print(obj[now.count(0)])
