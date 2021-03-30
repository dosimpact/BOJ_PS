from sys import stdin, setrecursionlimit
from itertools import combinations
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

# NM 모양찾기, 01 중 하나로 구성
# 컴포넌트 지정 및 넘버링
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
check = [[-1 for _ in range(M)] for _ in range(N)]
comp_counter = -1
comp_cnt_list = [0 for _ in range(1+N*M//2)]


def BFS(sx, sy, comp):
    total = 1
    dq = deque()
    dq.append((sx, sy))
    check[sx][sy] = comp
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            nx, ny = x+dx, y+dy
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if check[nx][ny] != -1:
                continue
            if graph[nx][ny] == 0:
                continue
            check[nx][ny] = check[x][y]
            dq.append((nx, ny))
            total += 1
    return total


def inRange(nx: int, ny: int):
    return (0 <= nx < N and 0 <= ny < M)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and check[i][j] == -1:
            comp_counter += 1
            res = BFS(i, j, comp_counter)
            comp_cnt_list[comp_counter] += res

ans_max = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            nearComp = set()
            for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                nx, ny = i+dx, j+dy
                if not inRange(nx, ny):
                    continue
                if check[nx][ny] == -1:
                    continue
                nearComp.add(check[nx][ny])
            ans_max = max(ans_max, sum(
                map(lambda x: comp_cnt_list[x], nearComp))+1)
print(ans_max)
