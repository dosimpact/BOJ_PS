from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# N개의 종이로 가린다.
# M개 넘개 겹쳐야 안보임

N, M = map(int, input().split())
graph = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            graph[i][j] += 1

cnt = 0
for row in graph:
    cnt += len(list(filter(lambda x: x > M, row)))
print(cnt)
