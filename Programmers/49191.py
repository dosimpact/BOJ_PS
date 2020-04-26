

import sys


def input(): return sys.stdin.readline().rstrip()

"""


"""
Graph = []
"""
[
    [ (0,2) ] # 0번인덱스
]
"""


def solution(n, results):
    global Graph
    Graph = [[] for _ in range(n)]
    for w, l in results:
        Graph[w-1].append((0, l-1))  # 위너의 진 상대들
        Graph[l-1].append((1, w-1))  # 루저의 형님들
    # print(Graph)
    answer = 0

    for start in range(n):
        loswin = [0]*2
        check = [False]*n
        q = [(0, start), (1, start)]
        check[start] = True
        while q:
            (nowisgud, now) = q.pop(0)
            for (isgud, who) in Graph[now]:
                # 현재 스테이트 같고, 방문 안했다면
                if nowisgud == isgud and not check[who]:
                    check[who] = True
                    loswin[nowisgud] += 1
                    q.append((isgud, who))
        #print(f"{start}  >  {loswin}")
        if sum(loswin) == n-1:
            answer += 1
    return answer


print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
