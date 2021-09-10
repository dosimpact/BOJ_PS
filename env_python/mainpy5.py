def inputData():
    total_map = []
    N, M = map(int, input().split())
    for i in range(N):
        total_map.append(list(map(int, input().split())))
    return N, M, total_map


def findIsland(mapData, row, col):
    land = 2
    for i in range(row):
        for j in range(col):
            if mapData[i][j] == 1:
                mapData = bfs(mapData, i, j, land)
                land = land + 1
    return mapData, land


def bfs(mapData, y, x, mark):
    visited[y][x] = 1
    mapData[y][x] = mark
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < col and 0 <= ny < row:
                if visited[ny][nx] == 0 and mapData[ny][nx] == 1:
                    mapData[ny][nx] = mark
                    visited[ny][nx] = 1
                    queue.append((nx, ny))
    return mapData


def findIslandlen(mapData, row, col):
    for i in range(row):
        for j in range(col):
            if mapData[i][j] != 0:
                dfs_straight(mapData, i, j)


def dfs_straight(mapData, sy, sx):
    start = mapData[sy][sx]
    queue.append((sx, sy))
    while queue:
        sx, sy = queue.pop()
        for i in range(4):
            len = 0
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < col and 0 <= ny < row:
                if mapData[ny][nx] == 0:
                    queue.append((nx, ny))
                    len = len + 1
                    while 1:
                        x, y = queue.pop()
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < col and 0 <= ny < row:
                            if mapData[ny][nx] == 0:
                                queue.append((nx, ny))
                                len = len + 1
                            elif mapData[ny][nx] != start:
                                if len > 1 and visited[start][mapData[ny][nx]] > len:
                                    visited[start][mapData[ny][nx]] = len
                                break
                            else:
                                break
                        else:
                            break


# union find에 필요한 함수
def get_parent(x, parent):
    if x == parent[x]:
        return x
    parent[x] = get_parent(parent[x], parent)
    return parent[x]


def union_find(y, x, parent):
    y = get_parent(y, parent)
    x = get_parent(x, parent)
    parent[x] = y


row, col, imap = inputData()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * col for _ in range(row)]
queue = []

imap, land = findIsland(imap, row, col)


visited = [[20] * land for _ in range(land)]
findIslandlen(imap, row, col)


# print(visited)

parent = [0] * (land)
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(2, land):
    parent[i] = i

for i in range(land):
    for j in range(land):
        if i <= j:
            continue
        if visited[i][j] == 20:
            continue
        edges.append((visited[i][j], i, j))
edges.sort()

for value, y, x in edges:
    # 두 섬이 '직접 / 간접' 어느 것으로든 연결되어 있지 않은 경우
    if get_parent(y, parent) != get_parent(x, parent):
        # 두 섬을 union_find로 연결한다.
        union_find(y, x, parent)
        result += value


if result == 0:
    result = -1

tmp = parent[2]
for i in range(3, land):
    if parent[i] != tmp:
        result = -1


print(result)


"""
for i in range(row):
    print(imap[i])
"""

