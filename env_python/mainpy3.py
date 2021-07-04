import math
from collections import deque
r, c, t = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))


def pure_on(a, c):
    global graph
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])
    for i in range(a - 1, -1, -1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 2, - 1, -1):
        temp_list.append(graph[0][i])
    for i in range(1, a):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)

    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a - 1, -1, -1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 2, - 1, -1):
        graph[0][i] = q.popleft()
    for i in range(1, a):
        graph[i][0] = q.popleft()


def pure_on_2(a, c):
    temp_list = []
    for i in range(1, c):
        temp_list.append(graph[a][i])

    for i in range(a + 1, r - 1):
        temp_list.append(graph[i][c - 1])
    for i in range(c - 1, - 1, -1):
        temp_list.append(graph[r - 1][i])
    for i in range(r - 2, a - 1, -1):
        temp_list.append(graph[i][0])

    temp_list.insert(0, 0)
    del temp_list[-1]

    q = deque(temp_list)

    for i in range(1, c):
        graph[a][i] = q.popleft()
    for i in range(a + 1, r - 1):
        graph[i][c - 1] = q.popleft()
    for i in range(c - 1, - 1, -1):
        graph[r - 1][i] = q.popleft()
    for i in range(r - 2, a - 1, -1):
        graph[i][0] = q.popleft()
    graph[a][0] = -1


def check(x, y):
    if 0 <= x < r and 0 <= y < c:
        if graph[x][y] != -1:
            return True
    return False


for _ in range(t):
    spd = []
    pure = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 or graph[i][j] != -1:
                if graph[i][j] >= 5:
                    spd.append((i, j))
            if graph[i][j] == -1:
                pure.append([i, j])
    plus = []
    for x, y in spd:
        cnt = 0
        if check(x - 1, y) == True:
            plus.append([x-1, y, math.floor(graph[x][y] / 5)])
            cnt += 1
        if check(x, y - 1) == True:
            plus.append([x, y - 1, math.floor(graph[x][y] / 5)])
            cnt += 1
        if check(x + 1, y) == True:
            plus.append([x + 1, y, math.floor(graph[x][y] / 5)])
            cnt += 1
        if check(x, y + 1) == True:
            plus.append([x, y + 1, math.floor(graph[x][y] / 5)])
            cnt += 1

        graph[x][y] = graph[x][y] - math.floor(graph[x][y] / 5) * cnt
        if graph[x][y] <= 0:
            graph[x][y] = 0

    for x, y, z in plus:
        graph[x][y] += z
    pure_cnt = 1

    for a, b in pure:

        if pure_cnt == 1:
            pure_on(a, c)
            pure_cnt += 1
        elif pure_cnt == 2:
            pure_on_2(a, c)

total = 0
for i in range(r):
    # print(graph[i])
    total += sum(graph[i])
print(total + 2)
