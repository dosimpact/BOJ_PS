"""
https://www.acmicpc.net/problem/4991

로봇 청소기

-방문할수없는 더러운칸
-전부 깨끗한 경우
...
.o.
...
"""

import sys
import itertools

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        exit(0)

    graph = [list(input()) for _ in range(n)]
    flags = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                flags.insert(0, (i, j))
            if graph[i][j] == '*':
                flags.append((i, j))

    if len(flags) == 1:
        print(0)
        continue
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 인접한칸  != 대각선 이동
    # dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    # dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    meta = [[] for _ in range(len(flags))]
    isposs = True

    for i in range(len(flags)):
        check = [[-1 for _ in range(m)] for _ in range(n)]
        start_x, start_y = flags[i]
        check[start_x][start_y] = 0
        q = []
        q.append((start_x, start_y))
        while len(q) != 0:
            x, y = q.pop(0)
            for k in range(len(dx)):
                nx, ny = (x+dx[k], y+dy[k])
                # 범위 체크, 방문 여부 체크 ,-> 방문해주고 큐에 넣어주기
                if (nx >= 0 and ny >= 0 and nx < n and ny < m) and check[nx][ny] == -1 and graph[nx][ny] != 'x':
                    check[nx][ny] = check[x][y]+1
                    q.append((nx, ny))

        for j in range(len(flags)):
            x, y = flags[j]
            if(check[x][y] == -1):
                isposs = False
            meta[i].append(check[x][y])

    if not isposs:
        print(-1)
        continue

    routes = list(itertools.permutations([i for i in range(1, len(flags))]))

    ans_min = -1

    for route in routes:
        ans_tmp = 0
        rs = list(route)
        rs.insert(0, 0)
        if DEBUG:
            print("4-->rs : ", rs)
        # 0 1 2 3

        for idx in range(len(rs)-1):
            ans_tmp += meta[rs[idx]][rs[idx+1]]
        if DEBUG:
            print("5--> ans_tmp", ans_tmp)
        if ans_min == -1 or ans_min > ans_tmp:
            ans_min = ans_tmp

    print(ans_min)
