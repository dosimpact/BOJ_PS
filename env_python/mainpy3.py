import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  # (1,1 ) ~ (N,N)
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))


# ST1. DFS 로 bug 검색하자
# visited stack 을 통해서, 싸이클을 판단할 수 있다.

check = [0] * (N+1)
visitedStack = [0] * (N+1)


def DFS(x):
    global visitedStack
    check[x] = 1
    visitedStack[x] = 1
    for (nxt, nxtW) in graph[x]:
        if nxt != 0 and check[nxt] == 0:
            if DFS(nxt):
                return True
        elif visitedStack[nxt]:
            return True
    visitedStack[x] = 0
    return False


res = DFS(1)
if res or check[N] == 0:
    print("bug")
    exit(0)

# ST2. BUG 가 없다는 것은, 한 방향으로 그래프가 수렴을 하는거시니, 완전 탐색을 통해서, 최소값 (BFS) 를 찾아내자.

check = [9999999999] * (N+1)

check[1] = 0
q = [1]
while q:
    now = q.pop(0)
    for next, nextW in graph[now]:
        check[next] = min(check[now] + nextW, check[next])
        q += [next]
# print(check)
print(check[N])

"""
3 3
2 3 -3
1 3 9
1 2 10

3 4
2 3 -3
1 3 9
1 2 10
3 1 1

3 3
2 3 3
1 3 9
1 2 10

3 3
2 2 3
2 1 9
1 2 10

3 3
1 1 3
2 2 9
3 3 10


4 3
1 2 3
2 4 9
3 4 10

4 4
1 2 3
2 4 9
3 4 10
1 4 -1

5 5
1 2 1
2 5 1
2 3 -1
3 4 -1
4 2 -1

"""
