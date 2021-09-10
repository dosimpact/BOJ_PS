import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 입력
N = int(input())
T = [0]
P = [0]
for _ in range(N):
    u, v = map(int, input().split())
    T.append(u)
    P.append(v)

D = [0 for i in range(N + 2)]
M = 0  # 그전 상담으로 제공해주는 최소 금액
for today in range(1, N+1):
    # i일 상담을 한다.
    nxtday = today + T[today]
    M = max(M, D[today-1])
    D[today] = max(D[today], M)
    if nxtday <= N+1:
        # print(f"today {today} > nxtday {nxtday} {D[today] + P[today]} M({M})")
        D[nxtday] = max(M, D[nxtday], D[today] + P[today])
        # for j in range(nxtday, N+2, 1):
        # D[j] = max(D[j], D[today] + P[today])

print(D)
print(max(D))
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""
