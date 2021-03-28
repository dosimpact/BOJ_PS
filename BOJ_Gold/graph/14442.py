from collections import deque

# 10**7

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

check = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

# check 선언,벽을 부시고 이동 or 그냥 이동 둘다 가능

dq = deque()
check[0][0][0] = 1
dq.append((0, 0, 0))

while dq:
    x, y, w = dq.popleft()  # x,y 위치 와, 현재 가중치
    # 벽안부시고 이동
    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
        nx, ny = x+dx, y+dy
        if not(0 <= nx < N and 0 <= ny < M):
            continue
        if check[nx][ny][w] == 0 and graph[nx][ny] == 0:
            check[nx][ny][w] = check[x][y][w] + 1
            dq.append((nx, ny, w))

        if w+1 <= K and check[nx][ny][w+1] == 0 and graph[nx][ny] == 1:
            check[nx][ny][w+1] = check[x][y][w] + 1
            dq.append((nx, ny, w+1))


res = [e for e in check[N-1][M-1] if e != 0]
if len(res) == 0:
    print(-1)
else:
    print(min(res))
# 의문 - 벽을 부셔서 graph에 기록을 안하면 부신거 또 부신다.
