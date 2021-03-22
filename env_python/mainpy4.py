import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
check = [[False for _ in range(M)] for _ in range(N)]
ans_max = 1

# 현재 x,y에 방문해 있다.
def DFS(x: int, y: int, log: str, span: int):
    # print(f"x,y,log,span {x,y,log,span}")
    global ans_max, check
    # 조건을 현재 노드에서 검사해서, 콜스택 최적화
    # 범위 체크, 중복 방문 체크, 로그 체크
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if check[nx][ny] == True:
            continue
        if graph[nx][ny] in log:
            continue
        check[nx][ny] = True
        ans_max = max(ans_max, span + 1)
        DFS(nx, ny, log + graph[nx][ny], span + 1)
        check[nx][ny] = False


check[0][0] = True
DFS(0, 0, graph[0][0], 1)
check[0][0] = False
print(ans_max)
"""
3 6
HFDFFB
AJHGDH
DGAGEH
>✅ 4
>6


4 4
AAAH
BAAG
CDEF
AAAF
>✅ 3 - 다음 DFS 호출할때 현재 노드로 했다.
>8
"""