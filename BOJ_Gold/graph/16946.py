from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# N,M 행렬, 0이동가능,1벽

# (NM)(NM) = (각벽마다)(BFS) > 시간초과
# (NM)+(NM) = (0의컴포넌트수)+(상하좌우덧셈)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

comp_count = -1
comp_cnt_list = [0 for _ in range(1+N*M//2)]
check = [[-1 for _ in range(M)] for _ in range(N)]
# 0이 컴포넌트 분리, 각 넘버마다 갯수 저장


def BFS(sx, sy, comp):
    dq = deque()
    check[sx][sy] = comp
    dq.append((sx, sy))
    total = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            nx, ny = x+dx, y+dy
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if check[nx][ny] != -1:
                continue
            if graph[nx][ny] == '1':
                continue
            check[nx][ny] = check[x][y]
            dq.append((nx, ny))
            total += 1
    return total


for i in range(N):
    for j in range(M):
        if graph[i][j] == '0' and check[i][j] == -1:
            comp_count += 1
            res = BFS(i, j, comp_count)
            comp_cnt_list[comp_count] += res

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            print(0, end="")
        else:
            comp_set = set()
            for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                nx, ny = i+dx, j+dy
                if not(0 <= nx < N and 0 <= ny < M):
                    continue
                comp_set.add(check[nx][ny])
            res = (sum(map(lambda x: comp_cnt_list[x], comp_set)) + 1) % 10
            print(res, end="")
    print()

"""
4 5
00000
00000
00000
00000

4 5
11111
11111
11111
11111

4 5
11001
00111
01010
10101
"""
