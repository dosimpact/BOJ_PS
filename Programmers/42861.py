
import sys
sys.setrecursionlimit(10**6)


def solution(n, costs):
    costs.sort(key=lambda e: e[2])
    check = [-1 for _ in range(n)]
    component = 1
    ansMin = 0
    leftBri = n-1
    # 우선 최소로 다 연결
    for cost in costs:
        u, v = cost[0], cost[1]
        if check[u] == -1 and check[v] == -1:  # 둘다 연결이 안된경우 | 새로운 컴포넌트 만들고 | 공사비 지불
            check[u] = check[v] = component
            component += 1
            ansMin += cost[2]
            leftBri -= 1
        elif check[u] == -1 or check[v] == -1:
            cNum = max(check[u], check[v])
            check[u] = check[v] = cNum
            ansMin += cost[2]
            leftBri -= 1
        else:
            pass
    print(check)
    print(ansMin)
    print(leftBri)
    if leftBri == 0:
        return ansMin

    checkC = [-1 for _ in range(component)]

    for cost in costs:
        u, v = cost[0], cost[1]
        # 둘다 연결이 안된경우 | 새로운 컴포넌트 만들고 | 공사비 지불
        if check[u] != check[v] and (checkC[check[u]] == -1 or checkC[check[v]] == -1):
            checkC[check[u]] = checkC[check[v]] = 1
            ansMin += cost[2]
            leftBri -= 1
        if leftBri == 0:
            break
    return ansMin


##print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(6, [[0, 1, 1], [2, 3, 2], [4, 5, 3], [0, 2, 4], [0, 4, 5]]))

"""
리스트 초기화는 for 문으로 해야한다. []*뭐시로 2중 리스트하면 안됨.!
graph = [[] for _ in range(len(words))]


별자리 알고리즘
"""
