import sys
from collections import deque

# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)


# 인구이동
# NN 땅 , 각 땅에는 나라가 하나씩 존재
# A[r][c] 명이 산다
# 인구 이동을 한다. 없을때 까지 아래 방법

# L <= 인구차이 <= R , 국경선 연다
# 인구는 mean으로 분배한다.
# 인구 이동 횟수는 ?

# 조건에 맞게끔 컴포넌트 수를 구한다.
# 컴포넌트 갯수만큼 인구 이동 연산을 수행
# 컴포넌트 수가 N*N개이면 종료

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
ans_cnt = 0
dq = deque()
while True:
    com_cnt = 0
    check = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:  # 컴포넌트 생성
                com_cnt += 1
                dq.clear()
                dq.append((i, j))
                check[i][j] = com_cnt
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                        nx, ny = x + dx, y + dy
                        if not (0 <= nx < N and 0 <= ny < N):
                            continue
                        if check[nx][ny] != 0:
                            continue
                        if not (L <= abs(graph[nx][ny] - graph[x][y]) <= R):
                            continue
                        check[nx][ny] = check[x][y]
                        dq.append((nx, ny))
    if com_cnt == N * N:
        break
    ans_cnt += 1
    for com in range(1, com_cnt + 1):
        res = [graph[i][j]
               for i in range(N) for j in range(N) if check[i][j] == com]
        poupuler_res = sum(res) // len(res)
        for i in range(N):
            for j in range(N):
                if check[i][j] == com:
                    graph[i][j] = poupuler_res
print(ans_cnt)


"""
2 20 50
50 30
20 40
"""
