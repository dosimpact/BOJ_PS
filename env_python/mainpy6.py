from collections import deque


N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
check = [[False for _ in range(M)] for _ in range(N)]
ans_max = 1

dq = set()
dq.add((0, 0, graph[0][0]))  # 좌표,로그 겸 길이
while dq:
    x, y, log = dq.pop()
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if graph[nx][ny] in log:
            continue
        ans_max = max(ans_max, len(log) + 1)
        dq.add((nx, ny, graph[nx][ny] + log))

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