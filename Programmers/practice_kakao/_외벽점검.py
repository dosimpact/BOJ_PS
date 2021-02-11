import sys
import copy

Debug = True

"""
그래프 만들기

# 인접행렬을 만들어서

# 인접 행렬의 내용 채우기 1.

# 특정 노드에서 부터 탐색을 시작하기,
재귀함수 작성

# 최소로 커버되는 답 출력

"""

distInitLen = 0
K = 0  # Node Len
check = []
graph = []
AnsMin = -1
People = []


def next(n: int, i: int):  # i == 0 오 | i == 1 왼
    if i == 0:
        if n+1 == K:
            return 0
        return n + 1
    else:
        if n - 1 == -1:
            return K-1
        return n-1


def dfs(now: int, check: [], di: int, bestP: int):  # 현재 노드 , check 상태, 방향, B
    check[now] = 1
    nnode = now
    LimitP = 0
    while True:
        # 이동해라
        LimitP += graph[nnode][di]
        nnode = next(nnode, di)
        #  커버 가능하냐?
        if LimitP <= bestP:
            check[nnode] = 1
        else:
            break
        # 혹시 끝났냐
        if check.count(0) == 0:
            return
    return


def go(now: int, check: [], pidx: int):  # 현재 노드, 체크 상태, 노동자
    global AnsMin

    # 최고 인력으로 now 노드에서, dfs를 해봄
    if check.count(0) == 0:
        if AnsMin == -1 or AnsMin > pidx+1:
            AnsMin = pidx+1
        print(f"Suc : {check} {AnsMin}")
        return
    # bc 사람이 없는 경우
    if check.count(0) != 0 and pidx == distInitLen:
        print(f"fail : {check} {AnsMin}")
        return
    if AnsMin != -1 and pidx+1 > AnsMin:
        print(f"fail : {check} {AnsMin}")
        return
    print(f" go {now} {check} {pidx} {AnsMin} BestP :{People[pidx]}")
    bestP = People[pidx]
    for i in range(2):
        newCheck = copy.deepcopy(check)
        dfs(now, newCheck, i, bestP)
        # 최고 인력으로 now 노드에서, dfs를 해봄
        if check.count(0) == 0:
            if AnsMin == -1 or AnsMin > pidx+1:
                AnsMin = pidx+1
            print(f"Suc : {check} {AnsMin}")
            return
        # bc 사람이 없는 경우
        if check.count(0) != 0 and pidx == distInitLen:
            print(f"fail : {check} {AnsMin}")
            return
        if AnsMin != -1 and pidx+1 > AnsMin:
            print(f"fail : {check} {AnsMin}")
            return
        # keep 다음 경우
        for j in range(K):
            if newCheck[j] == 0:
                go(j, newCheck, pidx+1)


def solution(n, weak, dist):
    global K, check, graph, distInitLen, People
    # init
    K = len(weak)  # 4
    check = [0]*K
    dist.sort(reverse=True)
    distInitLen = len(dist)
    People = dist
    graph = [[0 for _ in range(2)] for _ in range(K)]  # [K] [ 0 오른쪽 | 1 왼쪽 ]
    # make graph
    graph[0][0] = abs(weak[1] - weak[0])
    graph[0][1] = abs(0 - weak[0]) + abs(n - weak[-1])

    for i in range(1, len(weak) - 1):
        graph[i][0] = abs(weak[i] - weak[i+1])
        graph[i][1] = abs(weak[i] - weak[i-1])

    graph[K-1][0] = abs(weak[-1] - weak[-2])
    graph[K-1][1] = graph[0][1]

    print(graph)

    for i in range(len(weak)):
        print(f" entry {i} >")
        go(i, check, 0)
    return AnsMin


print(solution(12, [1, 3, 4, 9, 10]	, [3, 5, 7]))
#print(solution(12, [1, 5, 6, 10]	, [1, 2, 3, 4]))


"""
시간 초과 된다.
"""
