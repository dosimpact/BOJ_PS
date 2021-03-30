from sys import stdin, setrecursionlimit
from collections import deque
from typing import List, Tuple

input = stdin.readline
setrecursionlimit(10 ** 6)

# ❌1. 시간초과
# ❌2. 다른 아이디어발상

# N,M 격자칸 - 비거나, 막힘
# 플레이어 하나 이상의 성, 턴마다 확장
# Si 칸 만큼 확장

N, M, P = map(int, input().split())
S = list(map(int, input().split()))
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

# 각 플레이어마다 큐를 가진다. 1회차 돌림을 기준으로 p1원부터 탐색
ans_cnt = [0 for _ in range(P)]
q_list = [[] for _ in range(P)]  # 0 사용

for i in range(N):
    for j in range(M):
        if graph[i][j] == '.' or graph[i][j] == '#':
            continue
        idx = int(graph[i][j]) - 1
        q_list[idx].append((i, j))
        ans_cnt[idx] += 1


end_flag = [False for _ in range(P)]
while True:
    for i in range(P):  # i번 플레이어 처리
        for j in range(S[i]):  # 회수만큼 턴 -  10**9
            inTurnQ = q_list[i]
            q_list[i] = []
            if len(inTurnQ) == 0:
                end_flag[i] = True
                break
            while inTurnQ:
                x, y = inTurnQ.pop(0)
                for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0, ]):
                    nx, ny = x+dx, y+dy
                    if not(0 <= nx < N and 0 <= ny < M):
                        continue
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = str(i+1)
                        ans_cnt[i] += 1
                        q_list[i].append((nx, ny))
    if end_flag.count(True) == P:
        break
print(*ans_cnt)
"""
3 3 2
1 1
1..
...
..2
"""
