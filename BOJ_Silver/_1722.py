from math import factorial
import sys
from collections import deque
import math


def input(): return sys.stdin.readline().rstrip()


"""
4
1 10

4
2 2 3 4 1

"""


def go(now: int, n: int):
    if n == 0:
        return
    a, b = 0, factorial(n-1)
    for idx in range(n):
        if a <= now and now < b:
            ans.append(q[idx])
            q.pop(idx)
            go(now-a, n-1)
        a = b
        b += factorial(n-1)


def back(ori: [], wan: [], now: int, n: int):
    #print(f"{ori} {wan} {now} {n}")
    if n == 0:
        return now
    idx = ori.index(wan[0])
    wan.pop(0)
    ori.pop(idx)
    return back(ori, wan, now+factorial(n-1)*idx, n-1)


ans = []
#print(q, ans)
#print(back([0, 1, 2], [1, 2, 0], 0, 3))

N = int(input())
a, *b = map(int, input().split())
q = [i for i in range(1, N+1)]
if a == 1:
    go(b[0], N)
    print(*ans)
else:
    print(back(q, b, 0, N))
