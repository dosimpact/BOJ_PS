
import sys


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def GL(a, b):
    G = gcd(a, b)
    return G, (a*b)//G


(a, b) = map(int, input().split())

(l, g) = GL(a, b)
print(g)
