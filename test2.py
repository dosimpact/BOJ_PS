
import sys

"""
문제 :

방향성도 따져야 하지만,
파이프의 모양은 ?

1 STEP:
현재의 좌표, 방향, 블럭

다음 좌표,방향, 블럭
"""
Debug = True


def input(): return sys.stdin.readline().strip()


# (블럭) = (내방향 인덱스)
di = {
    '1': (1, -1, -1, 2),
    '2': (-1, -1, 1, 0),
    '3': (-1, 0, 3, -1),
    '4': (3, 2, -1, -1),
    '+': (0, 1, 2, 3),
    '-': (-1, 1, -1, 3),
    '|': (0, -1, 2, -1),
}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < r and y < c


"""
# 계속해서 돌다가, 
# 다음 위치가 빈 블럭인 경우 | 끝점에 도달한 경우 ( 모든 블럭을 안이용, 혹은 이용 )

# 현재 위치 + 현재 방향 > 현재 블럭 > 다음 방향 > 다음 위치 - 다음 블럭
"""


def bfs(x: int, y: int, drc: int):
    # bfs 검색결과 : 마지막 위치 반환
    q = [(x, y, drc)]
    check[x][y] += 1
    cnt = 1
    while q:
        x, y, direct = q[0]
        block = str(graph[x][y])
        # if Debug:
        #     print(f">>>x,y,di,block {x},{y},{direct},{block}")
        ndi = di[block][direct]
        nx, ny = x+dx[ndi], y + dy[ndi]
        nblock = graph[nx][ny]
        # if Debug:
        #     print(f">>>xNEXT {nx},{ny},{ndi},{nblock}")
        if nblock == ".":
            return (nx, ny, 1)
        elif nblock == "Z" or nblock == "M":
            if cnt == TotalBlock:
                return (nx, ny, 0)
            else:
                return (nx, ny, -1)
        else:
            q.append((nx, ny, ndi))


r, c = map(int, input().split())
graph = [['.' for _ in range(c)] for _ in range(r)]
check = [[0 for _ in range(c)] for _ in range(r)]
# checkZ = [[0 for _ in range(c)] for _ in range(r)]
# checkM = [[0 for _ in range(c)] for _ in range(r)]
TotalBlock = 0
MStart = None
ZStart = None
# 그래프를 잘 꾸며줘
for i in range(0, r):
    rec = list(input())
    for j in range(0, c):
        if rec[j] != '.':
            TotalBlock += 1
            graph[i][j] = rec[j]
        if rec[j] == 'M':
            MStart = (i, j)
        if rec[j] == "Z":
            ZStart = (i, j)

# Z에서부터 추적을 할꺼임. 끊기는 곳까지. 후보를 구한다.
zRes = None
for k in range(4):
    x, y = ZStart[0]+dx[k], ZStart[1]+dy[k]
    if inRange(x, y) and graph[x][y] != '.':
        zRes = bfs(x, y, k)
        break
if Debug:
    print(f"TOFILL {zRes}")

fx, fy = zRes[0], zRes[0]
for block in ['1', '2', '3', '4', '+', '-', '|']:
    if Debug:
        print(f"block {block}")
    graph[fx][fy] = block
    for k in range(4):
        x, y = ZStart[0]+dx[k], ZStart[1]+dy[k]
        if inRange(x, y) and graph[x][y] != '.':
            zRes = bfs(x, y, k)
            break
    if Debug:
        print(f"zRes{zRes}")
    graph[fx][fy] = '.'


# 배수관이 이어져야할 부분에, BF로 넣어서 Z가 나오는지 판단 + 모든 송유관 거쳤는지 판단.

"""
3 7
.......
.M-.-Z.
.......
"""
