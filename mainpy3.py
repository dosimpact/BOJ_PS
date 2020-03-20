
"""
https://www.acmicpc.net/problem/3053

택시 기하학

거리가 => 그냥 x + y 축 길이

원점 > 길이가 1인 원은 > 거리가 x +y로 측정되니 
45도 기울어진 사각형이 나온다.

파이r제곱
2r제곱

"""

import sys
import math
import functools
import itertools

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


r = int(input())
print(round((math.pi)*(r**2), 6))
print(round(float((2)*(r**2)), 6))
