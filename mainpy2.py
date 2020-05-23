

import sys
from collections import deque
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()


"""
그래프 탐색
"""

check = []  # -1 이면 방문 안함, 그외면 자식 노드의 수(방문함+)
graph = []  # 연결된 자식 노드의 정보
N = 0  # 노드의 갯수


def dfs(num: int):
    global check
    res = 0
    haschild = False
    for child in graph[num]:
        if check[child] == -1:
            res += dfs(child)
            haschild = True
    if not haschild:
        check[num] = 1
        return 1
    check[num] = res
    # 결과적으로 check 채우기 < 자식 노드의 수
    return res


def solution(total_sp, skills):
    # 노드의 갯수, 그래프 셋업
    global N, check, graph
    N = len(skills)+1  # 6개
    check = [-1 for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for skill in skills:
        graph[skill[0]].append(skill[1])
    # print(graph)
    # dfs탐색을 다돌아 최상위 스킬이 아니더라도 괜춘/ 메모지해야됨
    answer = []
    for start in range(1, N+1):
        if check[start] == -1:
            dfs(start)
    #print("dfs 결과", check)
    w = total_sp / sum(check[1:])
    return list(map(lambda e: int(e*w), check[1:]))


print(solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))
