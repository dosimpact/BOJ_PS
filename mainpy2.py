

import sys
sys.setrecursionlimit(10**6)

Debug = False


def input(): return sys.stdin.readline().rstrip()

# 입력처리


def getTeamValue(s: []):
    xlist = []
    ylist = []
    for e in s:
        xlist.append(personXY[e][0])
        ylist.append(personXY[e][1])
    if Debug:
        print(f"team {s} is {xlist} {ylist}")
    return ((max(xlist) - min(xlist))+(max(ylist) - min(ylist)))*2


N, M = map(int, input().split())
personXY = []

for _ in range(N):
    u, v = map(int, input().split())
    personXY.append((u, v))

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        continue
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

if Debug:
    print(graph)
    print(personXY)
# 묶기 컴포넌트를 돌꺼야, 근데 cnt가 아니라, check했던 녀석을을 구해
check = [0]*N

team = []
for s in range(0, N):
    teamTmp = []
    if check[s] == 0:
        check[s] = 1
        teamTmp.append(s)
        q = [s]
        while q:
            now = q.pop(0)
            for nxt in graph[now]:
                if check[nxt] == 0:
                    check[nxt] = 1
                    teamTmp.append(nxt)
                    q.append(nxt)
    if teamTmp:
        team.append(teamTmp)
if Debug:
    print(team)
# minmax

teamValue = []
for t in team:
    res = getTeamValue(t)
    teamValue.append(res)
if Debug:
    print(teamValue)

print(max(teamValue))
"""
8 7
17 1
1 3
8 14
18 19
19 19
2 15
17 8
11 3
1 1
4 3
4 5
3 5
1 7
1 2
3 3

"""
