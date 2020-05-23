
import sys
from copy import deepcopy


def input(): return sys.stdin.readline().rstrip()

"""
1 1
1 4
4 4
4 1
-1 -1

1 1
1 3
3 1
-1 -1
"""


def Area(xpos: [], ypos: []):

    ypos.append(ypos.pop(0))
    res1 = 0
    for i in range(len(ypos)):
        res1 += xpos[i]*ypos[i]

    ypos.insert(0, ypos.pop())  # fb
    xpos.append(xpos.pop(0))

    res2 = 0
    for i in range(len(xpos)):
        res2 += xpos[i]*ypos[i]
    return abs(res1-res2)/2


pcnt = 0
xpos = []
ypos = []
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    xpos.append(x)
    ypos.append(y)
    pcnt += 1

fres = Area(xpos, ypos)
print(fres)


def input(): return sys.stdin.readline().rstrip()


<< << << < HEAD
print(ts)
while ts:
    print(heapq.heappop(ts))
>>>>>> > e5a1f31122671d69a4f30619dab57dd29da27a28
== == == =

an, am = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(an)]

bn, bm = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(bn)]

#print(A, B)

C = [[0 for j in range(bm)] for i in range(an)]

for i in range(an):
    for j in range(bm):
        res, it = 0, am
        for k in range(it):
            res += A[i][k]*B[k][j]
        C[i][j] = res

for e in C:
    print(*e)
>>>>>> > 84197e1f135d9cd9c9a067fe85dec0a791191f11
