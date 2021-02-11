import sys

sys.setrecursionlimit(10**8)
Debug = False

N = 0
ans = 0
graph = []


def canPut(x: int, y: int):
    # 왼쪽으로 쭉 검사
    cx, cy = x, y
    while cx >= 0:
        if graph[cx][cy] == 1:
            return False
        cx -= 1

    # 대각선으로 쭉 검사
    cx, cy = x, y
    while cx >= 0 and cy >= 0:
        if graph[cx][cy] == 1:
            return False
        cx -= 1
        cy -= 1
    # 대각선으로 쭉 검사
    cx, cy = x, y
    while cx >= 0 and cy < N:
        if graph[cx][cy] == 1:
            return False
        cx -= 1
        cy += 1
    return True


def go(row: int):
    global ans, graph
    # BC 끝까지 도달한 경우
    if row == N:
        ans += 1
        return
    # 해당 자리에 두는 경우 | 안두는 경우
    for col in range(0, N):
        if canPut(row, col):
            graph[row][col] = 1
            go(row+1)
            graph[row][col] = 0


def solution(n):
    global graph, N
    N = n
    graph = [[0 for _ in range(N)] for _ in range(N)]
    go(0)
    return ans


print(solution(4))


"""
NQueen

스도쿠 처럼 > Z 을 하나씩 늘려가면서 해봄..
물론 stack의 깊이는깊어지고, 가는 길이 1개긴 한데, stack 생성 삭제가 오버헤드가 큰듯?


"""
