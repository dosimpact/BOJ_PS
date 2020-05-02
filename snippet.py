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
