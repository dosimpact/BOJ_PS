
import sys
import math
import functools
import itertools

DEBUG = True


sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()


n = int(input())
a = list(map(int, input().split()))

MAX = 5000
sumMAX = 400000

visited = [False]*sumMAX

res = 0
for i in range(n):
    for j in range(i):
        if visited[a[i] - a[j] + 200000]:
            res += 1
            break
    for j in range(i+1):
        visited[a[i]+a[j] + 200000] = True

print(res)
