import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


# 보드에 알파벳, 지금까지 새로운 알파벳만 밟기
# 1,1 시작해서 최대몇 이동 ?
# BFS 탐색 - check 배열 , check_alpha 딕셔너리 조건 추가 ❌
# DFS 탐색 접근 - 구지 다른 알파벳을 밟아서 최대거리를 깍지 말것


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
check = [[False for _ in range(C)] for _ in range(R)]
check_alpha = dict()
dq = deque()
dq.append((0, 0))
# check[0][0] = 1
# check_alpha[graph[0][0]] = True
ansMax = 0


def DFS(x: int, y: int, span: int):
    global ansMax
    if not(x >= 0 and y >= 0 and x < R and y < C):
        return
    if check[x][y]:
        return
    # ❌ dict 3가지 state,  존재하지 않을때, 존재할때 = True, 존재 안할때 False
    if graph[x][y] in check_alpha and check_alpha[graph[x][y]] == True:
        return

    ansMax = max(span, ansMax)

    check_alpha[graph[x][y]] = True
    check[x][y] = True
    #  for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        DFS(nx, ny, span+1)
    check[x][y] = False
    check_alpha[graph[x][y]] = False


DFS(0, 0, 1)
print(ansMax)
"""
❌ 다른답
3 6
HFDFFB
AJHGDH
DGAGEH
>❌ 4
>6

❌ 시간 초과
- check_alpha 배열로
- basecase는 함수 스택에 최대한 안쌓이도록 최적화
- 더 줄일려면 메모지에이션..?

2 4
CAAB
ADCB
>3

2 4
AAAB
ADCB
>1

2 4
ABCD
HGFE
>5

1 1
A
>1

4 4
AAAH
BAAG
CDEF
AAAF
>8
"""
