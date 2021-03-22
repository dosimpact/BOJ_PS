import sys

R, C = map(int, sys.stdin.readline().split())
db = [[e for e in sys.stdin.readline().strip()] for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

MAX = 1
queue = set([(0, 0, db[0][0])])
while queue and MAX < 26:
    x, y, history = queue.pop()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and (db[nx][ny] not in history):
            queue.add((nx, ny, history + db[nx][ny]))
            MAX = max(MAX, len(history) + 1)
print(MAX)