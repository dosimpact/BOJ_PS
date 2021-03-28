from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


N = int(input())
data = []
for _ in range(N):
    data.append(input().strip())
K = int(input())
for _ in range(K):
    kwd = input().strip()
    print(len([d for d in data if kwd in d]))
"""
5
dijkstra
greedy
bfs
backtracking
dynamic
3
bfs
greedyalgorithm
ra
"""