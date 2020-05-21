<<<<<<< HEAD
<<<<<<< HEAD
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
=======
import heapq
=======
import sys
>>>>>>> 1bb721091776b05cc993b770dfd9853db391c39a


def input(): return sys.stdin.readline().rstrip()

<<<<<<< HEAD
print(ts)
while ts:
    print(heapq.heappop(ts))
>>>>>>> e5a1f31122671d69a4f30619dab57dd29da27a28
=======

def mergeSort(ori: []):
    # BC
    if len(ori) <= 1:
        return
    # 분할 | merge recursion
    head = ori[:len(ori)//2]
    tail = ori[len(ori)//2:]
    mergeSort(head)
    mergeSort(tail)
    # 정복 | logic
    i, j, k = 0, 0, 0  # head, tail, ori 에 대한 포인터(사실 인덱스)
    while i < len(head) and j < len(tail):
        if head[i] < tail[j]:
            ori[k] = head[i]
            i += 1
        else:
            ori[k] = tail[j]
            j += 1
        k += 1
    while i < len(head):
        ori[k] = head[i]
        k += 1
        i += 1
    while j < len(tail):
        ori[k] = tail[j]
        k += 1
        j += 1


arr = [6, 15, 4, 1, 5, 5, 5, 29, 2, 3, 0]

print(arr)
mergeSort(arr)
print(arr)
>>>>>>> 1bb721091776b05cc993b770dfd9853db391c39a
