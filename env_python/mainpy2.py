import sys
import math
from typing import *
import itertools

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

first_arr = sorted(arr, key=lambda k: k[0])
second_arr = sorted(arr, key=lambda k: k[1])
answer = min(
    ((n//6) + 1) * first_arr[0][0],
    (n//6) * first_arr[0][0] + (n % 6) * second_arr[0][1],
    n * second_arr[0][1]
)
print(answer)
