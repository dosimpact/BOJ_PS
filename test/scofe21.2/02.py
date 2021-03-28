from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

# MST 문제, 간선의 정보들을 우선순위 큐에 저장
# 하나씩 꺼내면서 없으면 연결하기
# 문자열과 > 노드번호는 딕셔너리 테이블 이용

# ❌ 힙큐를 왜 이터레이터로 도냐!!

nameToNode = dict()
N = int(input())

cnt = 0
edges = []
for _ in range(N):
    u, v, w = input().split()
    if u not in nameToNode:
        nameToNode[u] = cnt
        cnt += 1
    if v not in nameToNode:
        nameToNode[v] = cnt
        cnt += 1
    edges.append((int(w), nameToNode[u], nameToNode[v]))


def getP(x: int):
    if x == parents[x]:
        return x
    parents[x] = getP(parents[x])
    return parents[x]


def union(x: int, y: int):
    px, py = getP(x), getP(y)
    if px < py:
        parents[py] = px
    else:
        parents[px] = py


def find(x: int, y: int):
    px, py = getP(x), getP(y)
    return px == py


parents = [_ for _ in range(cnt)]
edges.sort(key=lambda x: x[0])
# print(edges)
ans_min = 0
ans_cnt = 0
for w, u, v in edges:
    if not find(u, v):
        union(u, v)
        ans_min += w
        ans_cnt += 1
    if ans_cnt >= N:
        break
# print(nameToNode)
# print(ans_cnt)
print(ans_min)

"""
6
seoul beijing 3
beijing hawaii 10
seoul tokyo 4
seoul hawaii 6
tokyo hawaii 5
beijing tokyo 5

5
A B 1
C D 2
E F 3
A C 100
A E 100

9
A B 1
C D 2
E F 3
A C 10
A E 10
A C 100
A E 100
A C 500
A E 500
"""