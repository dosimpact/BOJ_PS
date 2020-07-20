from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    q.append([x, ""])
    c[x] = 1
    while q:
        x, d = q.popleft()
        if x == y:
            return d
        if 2*x <= 9999 and c[2*x] == 0:
            c[2*x] = 1
            q.append([2*x, d+'D'])
        if 2*x > 9999 and c[(2*x) % 10000] == 0:
            c[(2*x) % 10000] = 1
            q.append([(2*x) % 10000, d+'D'])
        if x-1 >= 0 and c[x-1] == 0:
            c[x-1] = 1
            q.append([x-1, d+'S'])
        if x-1 < 0 and c[9999] == 0:
            c[9999] = 1
            q.append([9999, d+'S'])
        nx = int((x % 1000) * 10 + x / 1000)
        if c[nx] == 0:
            c[nx] = 1
            q.append([nx, d+'L'])
        nx = int((x % 10) * 1000 + x / 10)
        if c[nx] == 0:
            c[nx] = 1
            q.append([nx, d+'R'])

tc = int(input())
while tc:
    c = [0 for _ in range(10000)]
    q = deque()
    x, y = map(int, input().split())
    ans = bfs(x)
    print(ans)
    tc -= 1