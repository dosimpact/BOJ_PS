

from collections import deque
import sys

SIZE = 101


def input(): return sys.stdin.readline().rstrip()


grpah = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
check = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]


def bfs():
    pass


m, n = map(int, input().split())

for i in range(n):
    for j in range(m):
        tmp = map(int, input())
        grpah[i] = tmp

for i in range(n):
    for j in range(m):
        print(grpah[i][j], end='')
    print()
