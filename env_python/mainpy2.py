"""
1:40~
- BFS/DFS quick 복습
[ 인접 행렬 | 인접 리스트 ver]
- 숨바꼭질
- 알고스팟
- 벽부스고 이동
- 이모티콘
"""


import sys


def input(): return sys.stdin.readline().rstrip()


n, m, v = map(int, input().split())

check = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]  # 0번 인덳 사용 X


"""
깊이 우선 탐색:
x방문 | 주변 노드 탐색 > 갈수 있으면 바로 간다.
너비 우선 탐색:
x방문 | q에 넣고, 주변노드들을 q에 저장해둔다. q를 꺼내서 방문하고, q를 또 넣어둔다

FB)
 - 문제의 변수와 커스텀 변수가 충돌이 일어남
.- global 선언했어야 한다.
"""


def dfs(x: int):
    global check
    check[x] = 1
    print(x, end=" ")
    for nxt in graph[x]:
        if check[nxt] == 0:
            check[nxt] = 1
            # print(nxt, end=" ")
            dfs(nxt)


def bfs(x: int):
    global check
    check[x] = 1
    q = []
    q.append(x)
    print(x, end=" ")
    while q:
        now = q.pop(0)
        for nxt in graph[now]:
            if check[nxt] == 0:
                check[nxt] = 1
                print(nxt, end=" ")
                q.append(nxt)
# DS 채워두기 + sorting


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()
# print(graph)
# BFS 탐색
dfs(v)
check = [0 for _ in range(n+1)]
print()
bfs(v)


"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
