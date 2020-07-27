import sys


def input(): return sys.stdin.readline().rstrip()


# https://www.acmicpc.net/problem/9328


T = int(input())
graph = []
keys = []
X, Y = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
sub_q = {}


def inRange(x, y):
    return x >= 0 and y >= 0 and x < X+2 and y < Y+2


for _ in range(T):
    X, Y = map(int, input().split())
    # =========== init ===========
    graph = [["."] + list(input()) + ["."] for _ in range(X)]
    graph.insert(0, ["." for _ in range(Y+2)])
    graph.append(["." for _ in range(Y+2)])
    check = [[0 for _ in range(Y+2)] for _ in range(X+2)]
    for key in range(ord('A'), ord('Z')+1):
        sub_q[chr(key)] = []
    keys = list(input())
    isKeyChange = True

    # 0,0 부터 BFS 로 탐색을 한다.
    check[0][0] = 0
    q = [(0, 0)]
    ans = 0
    while q:
        x, y = q.pop(0)
        # 서브 큐 추가
        if isKeyChange:
            for key in keys:
                if key == "0":
                    continue
                key = key.upper()
                if len(sub_q[key]) != 0:
                    while sub_q[key]:
                        q.append(sub_q[key].pop(0))
            isKeyChange = False

        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if not inRange(nx, ny) or check[nx][ny] != 0 or graph[nx][ny] == "*":
                continue
            # 다음이 벽인경우, 빈공간인 경우, 문서이 경우
            if graph[nx][ny] == ".":
                check[nx][ny] = 1
                q += [(nx, ny)]
            if graph[nx][ny] == "$":
                check[nx][ny] = 1
                q += [(nx, ny)]
                ans += 1
            # 문인 경우 - 열쇠가 있어, 없어
            if graph[nx][ny].isupper():
                check[nx][ny] = 1
                sub_q[graph[nx][ny]] += [(nx, ny)]
                isKeyChange = True
            # 열쇠인 경우
            if graph[nx][ny].islower():
                check[nx][ny] = 1
                q += [(nx, ny)]
                keys += [graph[nx][ny]]
                isKeyChange = True
                # sub_q[graph[nx][ny]] += [(nx, ny)]
    print(ans)
"""





3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
"""
