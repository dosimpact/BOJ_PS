from sys import stdin, setrecursionlimit
from collections import deque, defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)

# 0 빈칸, 1은 벽, 2는 바이러스 놓을 수 있는 칸
# 바이러스 1초마다 퍼짐
# M개 위치에 바이러스

# N 50
# M 10
# 250 C 10