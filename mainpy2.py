

import sys
from copy import deepcopy
from collections import defaultdict

sys.setrecursionlimit(10**8)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    check = [-1 for _ in range(n+1)]

    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    q = [1]
    check[1] = 1
    while q:
        now = q.pop(0)
        for next in graph[now]:
            if check[next] == -1:
                check[next] = check[now] + 1
                q.append(next)
    print(check)

    return check.count(max(check))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
