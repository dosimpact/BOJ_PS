V, E = map(int, input().split())
graph: List[List[int]] = [[] for _ in range(V + 1)]  # 0 사용 X
# edges = [list(map(int, input().split())) for _ in range(E)]
# edges.sort(key=lambda x: x[2])
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

check = [False for i in range(V + 1)]
pq = [(0, 1)]  # 가중치 0 으로, 1번노드부터 시작

ans = 0
while pq:
    # 현재 노드 에서 | 주변 탐색
    w, now = heapq.heappop(pq)
    if check[now]:  # 이미 방문해서 가중치 더함
        continue
    check[now] = True
    ans += w
    for nxt, nxt_w in graph[now]:
        if not check[nxt]:  # 아직 방문 안한 점이라면, pq 에 넣고 가능성을 보자.
            heapq.heappush(pq, (nxt_w, nxt))
print(ans)