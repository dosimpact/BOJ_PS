import sys


def input(): return sys.stdin.readline().rstrip()


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
T = int(input())
X, Y = 0, 0
graph = []


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < X+2 and y < Y+2


def BFS(check, start_x, start_y):
    check[start_x][start_y] = 0
    q = [(start_x, start_y)]

    while q:
        x, y = q.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not inRange(nx, ny) or check[nx][ny] != -1:
                continue
            if graph[nx][ny] == "." or graph[nx][ny] == "$":
                check[nx][ny] = check[x][y]
                q.insert(0, (nx, ny))
            if graph[nx][ny] == "#":
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))


for _ in range(T):
    X, Y = map(int, input().split())
    graph = [["."] + list(input()) + ["."] for _ in range(X)]
    check_out = [[-1 for _ in range(Y+2)] for _ in range(X+2)]
    check_1 = [[-1 for _ in range(Y+2)] for _ in range(X+2)]
    check_2 = [[-1 for _ in range(Y+2)] for _ in range(X+2)]
    graph.insert(0, ["." for _ in range(Y+2)])
    graph.append(["." for _ in range(Y+2)])

    # for row in graph:
    # print(*row)
    ppos = []
    for i in range(X+2):
        for j in range(Y+2):
            if graph[i][j] == "$":
                ppos.append((i, j))
    BFS(check_out, 0, 0)
    BFS(check_1, ppos[0][0], ppos[0][1])
    BFS(check_2, ppos[1][0], ppos[1][1])
    # for row in check_1:
    #     for e in row:
    #         print(e, end="\t")
    #     print()
    ans = []
    for i in range(X+2):
        for j in range(Y+2):
            if graph[i][j] == "*":
                continue
            tmp = check_out[i][j] + check_1[i][j] + check_2[i][j]
            if graph[i][j] == "#":
                tmp -= 2
            ans += [tmp]
    print(min(ans))
"""
빈 공간은 '.'
지나갈 수 없는 벽은 '*'
문은 '#'
죄수의 위치는 '$'

죄수 = 2명,
항상 밖으로 가는 경로 있다, .또는 #으로
두 죄수를 탈옥 시키기 위한 최소 문 열기 횟수

- 이동은 자유로움 cost = 0
- 문열기는 cost = 1
- 하지만 두 죄수의 union

- fromIdx => 죄수 1의 경로
- fromIdx => 죄수 2의 경로 
두 경로에서 문의 좌표를 set으로 만들어서 ,set1, set2 를 union 한다.

----------------------------------

*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********

*5**6**A*
*4**5**#*
*3**4**#*
*2**3**#*
*1*334*#*
*012*566*
*1*****5*
*1223344*
*********


9 9
*.**#**.*
*.**#**.*
*.**#**.*
*.**.**.*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********

"""
