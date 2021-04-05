from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# 싸이클 찾고, 싸이클이 아닌 노드에서 싸이클까지 거리
# 차수를 관찰 - 시작점을 알 수 있다.
# 차수가 높다고 , joint노드는 아니다.!!
# 1인 차수에서 BFS를 돌리고 cycle의 범위를 구한다.  - check배열
# dist 배열, 해당 범위는 q에 넣고 전부 0으로 만들고 BFS 돌리기

N = int(input())
graph = [[] for _ in range(N+1)]  # 0 unused
for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
check = [0 for _ in range(N+1)]
dq = deque()

for i in range(1, N):
    if len(graph[i]) == 1:
        dq.appendleft(i)
        check[i] = 1
        break
cycle_s, cycle_e = -1, -1

print(dq)
while dq:
    now = dq.popleft()
    for nxt in graph[now]:
        if check[nxt] != 0:
            if abs(check[nxt] - check[now]) == 1:
                continue
            else:
                print(f"now, nxt e{now, nxt}")
                print(f"check {check}")
                cycle_s, cycle_e = check[nxt], check[now]
                dq.clear()
                break
            continue
        check[nxt] = check[now]+1
        dq.append(nxt)

print(cycle_s, cycle_e)


"""
6
1 2
3 4
6 4
2 3
1 3
3 5
"""
