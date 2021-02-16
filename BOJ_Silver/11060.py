import sys
import math
import re
from typing import *

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
data = list(map(int, input().split()))
d = [math.inf for _ in range(N+101)]

d[0] = 0
for i in range(len(data)):
    jump = data[i]  # 0번위치에서 1번까지 점프가능
    for j in range(1, jump+1):  # 1번 점프부터
        d[i+j] = min(d[i+j], d[i]+1)
print(d[N-1]) if d[N-1] != math.inf else print(-1)
