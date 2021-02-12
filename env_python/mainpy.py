import sys
sys.setrecursionlimit(10**6)
# Union-Find (합집합 찾기) 알고리즘
# 자료구조 : 1차원 배열
# 목적 : 두 노드가 같은 집합인지 판단하기
# 1. find : 두 노드의 부모가 같니 ?
# 2. union : 두 노드를 합치기


graph = [i for i in range(10)]  # 1~9 까지 노드,
# graph[n]: n의 부모, graph[n] == n 이라면 초기상태 ( 연결없이 노드 하나 달랑있음 )

# 부모를 찾는다. ( 재귀로 )


def getParent(x: int):
    if graph[x] == x:
        return x
    graph[x] = getParent(graph[x])  # 부모정보 업데이트
    return graph[x]


def unionGrpah(x: int, y: int):
    Px = getParent(x)
    Py = getParent(y)
    if Px > Py:
        graph[Px] = Py
    else:
        graph[Py] = Px


def findGraph(x: int, y: int):
    Px = getParent(x)
    Py = getParent(y)
    if Px == Py:
        return True
    else:
        return False


print(f"graph : {graph}")
unionGrpah(1, 2)
print(f"graph : {graph}")
unionGrpah(2, 3)
print(f"graph : {graph}")
unionGrpah(1, 4)
print(f"graph : {graph}")
unionGrpah(5, 6)
print(f"graph : {graph}")
unionGrpah(6, 7)
print(f"graph : {graph}")
unionGrpah(7, 8)
print(f"graph : {graph}")

print(f" 1,4은 하나의 집합 ? {findGraph(1,4)}")
print(f" 5,6은 하나의 집합 ? {findGraph(5,6)}")
print(f" 4,5은 하나의 집합 ? {findGraph(4,5)}")
print(f" 1,8 은 하나의 집합 ? {findGraph(1,8)}")

unionGrpah(4, 5)
print(f"graph : {graph}")
print(f" 4,5 은 하나의 집합 ? {findGraph(4,5)}")
print(f" 1,8 은 하나의 집합 ? {findGraph(1,8)}")
print(f"graph : {graph}")
print(f"간선 정보 업데이트")
for _ in range(0, 10):
    getParent(_)
print(f"graph : {graph}")

"""
graph : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
graph : [0, 1, 1, 3, 4, 5, 6, 7, 8, 9]
graph : [0, 1, 1, 1, 4, 5, 6, 7, 8, 9]
graph : [0, 1, 1, 1, 1, 5, 6, 7, 8, 9]
graph : [0, 1, 1, 1, 1, 5, 5, 7, 8, 9]
graph : [0, 1, 1, 1, 1, 5, 5, 5, 8, 9]
graph : [0, 1, 1, 1, 1, 5, 5, 5, 5, 9]
 1,4은 하나의 집합 ? True
 5,6은 하나의 집합 ? True
 4,5은 하나의 집합 ? False
 1,8 은 하나의 집합 ? False
graph : [0, 1, 1, 1, 1, 1, 5, 5, 5, 9]
 4,5 은 하나의 집합 ? True
 1,8 은 하나의 집합 ? True
graph : [0, 1, 1, 1, 1, 1, 5, 5, 1, 9]
간선 정보 업데이트
graph : [0, 1, 1, 1, 1, 1, 1, 1, 1, 9]
 """
