
import sys
from collections import deque
input = sys.stdin.readline

# 지도 M,N
# 보물상자, 열쇠, 벽
# 상하좌우 이도
# 보물상자를 열 수 있는 지 여부
# 1. 열쇠를 획득해야함, 2. 보물상자를 획득해야함
# 0 빈칸, 1 벽, 2보물, 3, 소마 위치, 4 열쇠 위치

# 3이 이동한다 - 보물 획득, 열쇠 획득 가능하면 가능

graph = None
check = None
key, tra, start = None, None, None
N, M = None, None


def inRange(x: int, y: int):
    return x >= 0 and y >= 0 and x < N and y < M


def BFS():
    x, y = start
    check[x][y] = True
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            # 범위 체크, 벽체크, 방문 체크
            nx, ny = x+dx, y+dy
            # print(f"x, y {x, y} nx, ny {nx, ny} N,M {N,M}")
            # if not(dx >= 0 and dy >= 0 and dx < N and dy < M):
            # continue
            if not inRange(nx, ny):
                continue
            if check[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            check[nx][ny] = True
            dq.append((nx, ny))


def main():
    global graph, check, key, tra, start, N, M
    case = int(input())
    for _ in range(case):
        N, M = map(int, input().split())
        graph = []
        check = [[False for _ in range(M)] for _ in range(N)]
        for _ in range(N):
            graph.append(list(map(int, input().split())))
        key, tra, start = None, None, None
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2:
                    tra = (i, j)
                if graph[i][j] == 3:
                    start = (i, j)
                if graph[i][j] == 4:
                    key = (i, j)

        BFS()
        if check[key[0]][key[1]] and check[tra[0]][tra[1]]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()


"""
2
5 6
0 0 1 0 2 0
1 0 1 0 0 0
0 0 1 1 1 0
0 3 0 1 0 0
4 0 0 0 0 0
5 6
0 0 1 0 2 0
1 0 1 0 0 0
0 0 1 1 1 0
0 3 0 1 0 0
4 0 0 1 0 0
>
1
0


1
5 6
0 0 1 0 2 0
1 0 1 0 0 0
0 0 1 1 1 0
0 3 0 1 0 0
4 0 0 0 0 0
>1

1
5 6
0 0 1 0 2 0
1 0 1 0 0 4
0 0 1 1 1 1
0 3 0 1 0 0
0 0 0 0 0 0
>0

1
5 6
0 0 1 0 2 0
1 0 1 0 0 4
0 0 1 1 1 1
0 3 0 1 0 0
0 0 0 0 0 0
"""
