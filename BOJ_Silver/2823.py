"""
유턴 싫어 -> 문제 변형하기
"""


import sys


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())


graph = [list(input()) for _ in range(n)]

isposs = True

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '.':
            anotherDot = 0
            for k in range(4):
                (nx, ny) = (i+dx[k], j+dy[k])
                if (nx >= 0 and ny >= 0 and nx < n and ny < m) and (graph[nx][ny] == '.'):
                    anotherDot += 1
            if anotherDot < 2:
                isposs = False
        if not isposs:
            print(1)
            exit(0)

print(0)

"""
3 9
...XXX...
.X.....X.
...XXX...

"""
