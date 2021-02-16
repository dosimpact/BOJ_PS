import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


pos = list(map(int, input().split()))
A = [pos[0], pos[1]]
B = [pos[2], pos[3]]
C = [pos[4], pos[5]]
D = [pos[6], pos[7]]
low, high = 0, 100


def mPoint(p):  # A,B > 내분점
    return (A[0] + (B[0] - A[0])*(p/100), A[1] + (B[1] - A[1])*(p/100))


def gPoint(p):  # C,D > 내분점
    return (C[0] + (D[0] - C[0])*(p/100), C[1] + (D[1] - C[1])*(p/100))


ans = math.inf
while high - low >= 1e-6:
    p = (low*2+high*1)/3
    q = (low*1+high*2)/3

    m_pPoint = mPoint(p)
    m_qPoint = mPoint(q)
    g_pPoint = gPoint(p)
    g_qPoint = gPoint(q)

    # p에서 민호강호 거리
    dist_p = (m_pPoint[0] - g_pPoint[0])**2 + (m_pPoint[1] - g_pPoint[1])**2
    dist_q = (m_qPoint[0] - g_qPoint[0])**2 + (m_qPoint[1] - g_qPoint[1])**2
    dist_p = math.sqrt(dist_p)
    dist_q = math.sqrt(dist_q)
    ans = min(dist_p, dist_q)
    if dist_p > dist_q:
        low = p
    else:
        high = q
print("%0.10f" % ans)
"""
print((10)**(-6))
print(1e-06)
"""
