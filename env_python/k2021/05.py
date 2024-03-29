from copy import deepcopy
from collections import deque
# check[N번 노드][N개의 양을 가지고 방문] = T|F
N = None
graph, check = None, None
Edges, Info = None, None

# deepcopy 로 해보고, 시간,메모리 오류시 비트마스크로 변경


def BFS():
    check[0][1][0] = 1  # 0번 노드는 항상 루트|양이 있음|늑대는 없음
    q = deque()
    q.append((0, 1, 0, deepcopy(Info)))  # [ 노드의 위치,현재 모은 양의수 ,현재 모은 늑대의 수]
    while q:
        now = q.popleft()  # now[0] - 현재 위치, now[1] 현재 모은 양
        curSleep, curWorf = now[1], now[2]
        copyInfo = now[3]
        for nxtNode in graph[now[0]]:
            # print(f"{now[0]}->{nxtNode}")
            # input()
            # 다음 노드가 비어 있는 경우
            if copyInfo[nxtNode] == -1:
                if check[nxtNode][curSleep][curWorf] == 0:
                    check[nxtNode][curSleep][curWorf] = 1
                    nxtInfo = deepcopy(copyInfo)
                    q.append((nxtNode, curSleep, curWorf, nxtInfo))
            else:
                # 다음 노드가 늑대인 경우
                nxtInfo = deepcopy(copyInfo)
                if copyInfo[nxtNode] == 1:
                    # - 양이 안잡아먹히면 고
                    if curSleep > curWorf + 1:
                        if check[nxtNode][curSleep][curWorf+1] == 0:
                            nxtInfo[nxtNode] = -1
                            check[nxtNode][curSleep][curWorf+1] = 1
                            q.append(
                                (nxtNode, curSleep, curWorf+1, nxtInfo))
                    # 다음 노드가 양인 경우
                else:
                    if check[nxtNode][curSleep+1][curWorf] == 0:
                        nxtInfo[nxtNode] = -1
                        check[nxtNode][curSleep+1][curWorf] = 1
                        q.append(
                            (nxtNode, curSleep+1, curWorf, nxtInfo))


def solution(info, edges):
    global N, check, Info, Edges, graph
    Info, Edges = info, edges
    N = len(info)  # 0~11 인덱스로, 12개의 노드가 있다.
    check = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    BFS()
    # 루트 노드에 찍힌 방문 기록을 본다.
    ansMax = 0
    for idx, c in enumerate(check[0]):
        # idx 마리의 양을 모은 경우
        if c.count(1) >= 1:
            ansMax = max(ansMax, idx)
    return ansMax


# print(
#     solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#              [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
# )
# print(
#     solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#              [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [
#                  2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
#              )
# )
