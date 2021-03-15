from sys import setrecursionlimit, stdin
from math import inf
import heapq


input = stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
dist = [inf for _ in range(V + 1)]
check = [False for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

pq = [(0, K)]  # (이 가중치로 갈 수 있다, 이 노드 (번호) 를 )
dist[K] = 0
while pq:
    now_w, now = heapq.heappop(pq)
    if check[now]:
        continue
    check[now] = True
    for nxt, nxt_w in graph[now]:
        # 비교하기 - 바로가는것과, 거처가는것
        if dist[nxt] > dist[now] + nxt_w:
            dist[nxt] = dist[now] + nxt_w
            heapq.heappush(pq, (dist[nxt], nxt))

for d in dist[1:]:
    if d == inf:
        print("INF")
    else:
        print(d)
"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""