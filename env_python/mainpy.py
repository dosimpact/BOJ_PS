import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

LIMIT = 500000
N, K = map(int, input().split())
check = [[-1 for _ in range(2)] for _ in range(LIMIT + 1)]

dq = deque()
dq.append((N, 0))  # N을 0초에 방문 했다.
check[N][0] = 0

while dq:
    x, t = dq.popleft()  # x지점을 t(홀짝) 방문 했다
    for nx in [x + 1, x - 1, x * 2]:
        if not (0 <= nx <= LIMIT):
            continue
        if check[nx][1 - t] != -1:
            continue
        check[nx][1 - t] = check[x][t] + 1
        dq.append((nx, 1 - t))

ans = -1
t = 0
while K <= LIMIT:
    # 해당 시간(홀/짝)에 방문이 되어 있고, 대기중 혹은 마주친 경우라면
    if check[K][t % 2] != -1:
        if check[K][t % 2] <= t:
            ans = t
            break
    t += 1
    K += t
print(ans)
