# import sys
# import math
# from typing import *
# import itertools

# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

check = dict()


def BFS(x: int):
    q = [x]
    check[x] = 1
    while q:
        now = q.pop(0)
        if now > B:
            continue
        elif now == B:
            print(check[now])
            return True
        else:
            n1 = now*2
            if n1 not in check:
                check[n1] = check[now]+1
                q.append(n1)
            n2 = int(str(now)+"1")
            if n2 not in check:
                check[n2] = check[now]+1
                q.append(n2)
    return False


A, B = map(int, input().split())
if A == B:
    print(-1)
else:
    if not BFS(A):
        print(-1)
