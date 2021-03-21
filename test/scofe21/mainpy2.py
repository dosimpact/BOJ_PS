import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 방문해도 되는 1, 방문 X 는 0
#  한번에 1칸 혹은 2칸
# 왼 > 오 까지 몇가지 경우의 수?
# dp임

N = int(input())
data = input().strip()
d = [0 for _ in range(N)]
d[0] = 1
if data[1] == "1":
    d[1] = 1
for i in range(2, N):
    if data[i-1] != '0':
        d[i] += d[i-1]
    if data[i-2] != '0':
        d[i] += d[i-2]

print(d[N-1])
"""
3
111
>2


"""
