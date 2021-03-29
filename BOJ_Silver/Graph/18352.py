from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

# K만큼의 depth만
N, M, K, X = map(int, input().split())
grpah = [[] for _ in range(N + 1)]
check = [-1 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    grpah[u].append(v)


dq = deque()
dq.append(X)
check[X] = 0
ans = []
while dq:
    now = dq.popleft()
    for nxt in grpah[now]:
        if check[nxt] == -1:
            check[nxt] = check[now] + 1
            if check[nxt] == K:
                ans.append(nxt)
            elif check[nxt] < K:
                dq.append(nxt)

ans.sort()
if len(ans) == 0:
    print(-1)
else:
    for a in ans:
        print(a)