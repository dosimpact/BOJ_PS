
import sys
import math
import functools
import itertools

DEBUG = False


sys.setrecursionlimit(10**6)


#def input(): return sys.stdin.readline().rstrip()


buf = sys.stdin.read()
buf = list(map(int, buf.split()))
k = 0
nodes = []
linecnt = 0
while True:
    u = buf.pop(0)
    v = buf.pop(0)

    if u == -1:
        break
    if u == 0 and v == 0:
        k += 1
        nodes = list(set(nodes))
        if len(nodes) == 0 or len(nodes)-1 == linecnt:
            print(f'Case {k} is a tree.')
        else:
            print(f'Case {k} is not a tree.')
        nodes.clear()
        linecnt = 0
    else:
        linecnt += 1
        nodes.append(u)
        nodes.append(v)
