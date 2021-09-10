import sys
from collections import deque
from copy import deepcopy


input = sys.stdin.readline

N, K = map(int, input().split(" "))
points = []
for _ in range(N):
    x, y, k = map(int, input().split(" "))
    points.append((x, y, k))

print(points)


def getWidth(pointList):
    xlist = [e[0] for e in pointList]
    ylist = [e[1] for e in pointList]
    xSpan = abs(min(xlist) - max(xlist)) + 1
    ySpan = abs(min(ylist) - max(ylist)) + 1
    return xSpan * ySpan


# 경우의 수를 구하자.

# 점이 1개 골라진 경우 , 2개 골라진 경우 ... 다고른 경우 - 1번점에 대해서 , 그때의 배열

"""
5 2
-4 -2 1
-5 -3 1
5 -4 2
4 -5 2
3 -8 2
"""
