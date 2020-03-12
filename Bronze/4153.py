# https://www.acmicpc.net/problem/4153
import sys


def input(): return sys.stdin.readline().rstrip()


while True:
    a, b, c = map(int, input().split())
    if(a == b == c == 0):
        exit(0)
    mval = max([a, b, c])
    l1, l2 = filter(lambda x: x != mval, [a, b, c])
    if(mval**2 == (l1**2) + (l2**2)):
        print("right")
    else:
        print("wrong")
