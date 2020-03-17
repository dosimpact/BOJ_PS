"""
동기는 모두 N명
학번은 모두 1부터 N까지
상근이의 학번은 1이다.

인접리스트 오랜만에 써보자.
상근의의 친구 depth = 2 까지만 탐색하면 되지


6
7
1 2
1 3
2 4
6 5
3 4
2 3
4 5
"""

import sys


def input(): return sys.stdin.readline().rstrip()


# DFS 를 사용하면 안된다.

# def dfs(now: int, depth: int):
#     global check
#     if depth >= 3:
#         return

#     for nxt in graph[now]:
#         if check[nxt] == 0:
#             check[nxt] = depth+1
#             dfs(nxt, depth+1)

def bfs(now: int):
    global check
    q = []
    check[now] = 1
    q.append(now)
    while(len(q) != 0):
        cur = q.pop(0)
        for nxt in graph[cur]:
            if check[nxt] == 0:
                check[nxt] = check[cur] + 1
                if check[nxt] < 3:
                    q.append(nxt)


N = int(input())  # 동기의 수
M = int(input())  # 입력 횟수
graph = [[] for _ in range(N+1)]


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0 for _ in range(N+1)]
check[1] = 1
bfs(1)

print(check.count(2)+check.count(3), end='')

"""
FB)
결혼식 이문제 DSF 를 사용하면 안된다.
1 의 친구 2,3이 있는데, 
2,3 모두  1친인데, 
DFS 를 쓰게되면 1 -> 2 -> 3 의 과정으로 탐색을 하게 되고
그러면 1,3은 2친이 된다.

"""
