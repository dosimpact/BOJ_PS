from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# 싸이클 찾고, 싸이클이 아닌 노드에서 싸이클까지 거리
# 차수를 탐색하는 문제
