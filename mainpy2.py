

import sys
from copy import deepcopy
from collections import defaultdict

Debug = True
graph = None
cost = None


def solution(N, road, K):
    global graph, cost
    answer = 0
    # 마을의 정보를 인접 행렬로 만들자.  # 비용 행렬을 만들어서 초기값을 정해주자.
    graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]  # 그래프가 0 인거는 오케이
    cost = [[-1 for _ in range(N+1)] for _ in range(N+1)]  # cost는 -1 min처리

    for (u, v, w) in road:
        graph[u][v] = w
        graph[v][u] = w
        cost[u][v] = w
        cost[v][u] = w
    for i in range(1, N+1):
        cost[i][i] = 0

    # 최단거리로 비용행렬을 업데이트 하자.
    # 1 > k > 각마을

    u = 1
    for k in range(1, N+1):
        for v in range(1, N+1):
            if u == k or k == v:
                continue
            if graph[u][k] == -1 or graph[k][v] == -1:
                continue
            new_cost = cost[u][k] + cost[k][v]
            if cost[u][v] == -1:
                cost[u][v] = new_cost
            else:
                cost[u][v] = min(cost[u][v], new_cost)
    if Debug:
        for g in graph:
            print(*g)
        print("----")
        for g in cost:
            print(*g)
    cost[u][u] = 0
    for v in range(1, N+1):
        if cost[u][v] <= K:
            if Debug:
                print(f"u 1 > v {v} cost: {cost[u][v]}")
            answer += 1

    return answer


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))


"""
min 처리

"""
