import sys
from collections import deque

input = sys.stdin.readline

# 공간에 상품을 놓을 수 있는 경우의 수
# 정사각형 모양, 상품은 1x1 딱 한개
# 1*1 놓아볼래  > 경우의 수
# 2*2 놓아볼래 > 경우의 수
# dp , 가장 큰 정사각형

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))

d = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    if graph[0][i] == 1:
        d[0][i] = 1
    if graph[i][0] == 1:
        d[i][0] = 1

for i in range(1, N):
    for j in range(1, N):
        if graph[i][j] == 1:
            d[i][j] = 1
            adj_min = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
            d[i][j] = max(d[i][j], adj_min)


total = 0
total_list = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        for k in range(1, d[i][j]+1):
            total += 1
            total_list[k] += 1

print(f"total: {total}")
for i in range(len(total_list)):
    if total_list[i] == 0:
        continue
    print(f"size[{i}]: {total_list[i]}")

"""
4
1110
1110
0110
0000

5
11111
11111
01111
00011
11001


3
000
000
000
"""
