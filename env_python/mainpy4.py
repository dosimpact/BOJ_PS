# import sys
# import heapq
from heapq import heapify, heappop, heappush
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (x[0], x[1], x[2]))
check = [False for i in range(N)]  # 0 사용


def dist(p1, p2):  # 3차원 정점간  가중치
    return min(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2] - p2[2]))


# 프림 알고리즘
pq = [(0, 0)]  # (가중치,다음 노드)
heapify(pq)
ans = 0
cnt = 0  # for 메모리 다운
while pq:
    # print(f"pq {pq} | check {check}")
    w, now = heappop(pq)
    if check[now]:
        continue
    check[now] = True
    ans += w
    cnt += 1
    # 큐 클린
    if len(pq) > N//2:
        pq = list(filter(lambda x: not check[x[1]], pq))
    if cnt == N:
        break
    for i in range(N):
        if now == i:
            continue
        if check[i]:
            continue
        heappush(pq, (dist(data[i], data[now]), i))

print(ans)
