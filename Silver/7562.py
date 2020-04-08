
import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


"""
나이트의 이동

8 한변의 길이
00 나이트의 현재칸
70 목표 칸
"""

# bfs 탐색


t = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(t):
    L = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    check = [[-1 for _ in range(L)] for _ in range(L)]
    dq = deque()
    dq.append((sx, sy))
    check[sx][sy] = 0
    isEnd = False

    if sx == gx and sy == gy:
        print(0)
        continue

    while len(dq) > 0:
        x, y = dq.popleft()

        for k in range(len(dx)):
            nx, ny = x+dx[k], y+dy[k]
            if (nx >= 0 and ny >= 0 and nx < L and ny < L) and (check[nx][ny] == -1):
                check[nx][ny] = check[x][y] + 1
                dq.append((nx, ny))
                if nx == gx and ny == gy:
                    print(check[nx][ny])
                    isEnd = True
                    break
        if isEnd:
            break

"""
1
8
0 0
7 0
"""

arr = []
# 앞에서 넣고 뺴고
arr.pop(0)
arr.insert(0, 1)

# 뒤에서 넣고 빼고
arr.pop()
arr.append(1)

dq = deque()

# 앞에서 넣고 뺴고
dq.appendleft(1)
dq.popleft()

# 뒤에서 넣고 빼고
dq.append(1)
dq.pop()


"""
fb)


"""
