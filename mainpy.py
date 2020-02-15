
import sys


def input(): return sys.stdin.readline().rstrip()


SIZE = 51


def bfs(i):  # 현재 들어온애 진실 체크, 주변 인접 노드 탐색 및 방문 확인 | 방문시 진실 체크
    check[i] = 1
    q = []
    q.append(i)
    while len(q) != 0:
        now = q.pop(0)
        for next in graph[now]:
            if check[next] == -1:
                check[next] = 1
                q.append(next)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]  # 인접 리스트
count, *turman = map(int, input().split())
partyList = []
for _ in range(M):
    su, *partyPeople = map(int, input().split())
    partyList.append(partyPeople)
    for i in partyPeople:
        for j in partyPeople:
            if i == j:
                continue
            graph[i].append(j)

for it in graph:
    it = list(set(it))

check = [-1 for _ in range(N+1)]  # 진실을 아는 자들의 모임 1은 진실 1번 사람부터
for i in turman:
    bfs(i)

ans = 0
for i in partyList:
    cangura = True
    for person in i:
        if check[person] == 1:
            cangura = False
    if cangura:
        ans += 1
print(ans)
