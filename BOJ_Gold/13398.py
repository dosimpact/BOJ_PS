import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
P = list(map(int, input().split()))


d = [[0 for i in range(2)] for i in range(N)]  # i번째 수를 포함하는 수열의, 최대 합
d[0][0] = P[0]
d[0][1] = P[0]
for i in range(1, N):
    d[i][0] = P[i]  # 기본상태는 자기 자신, 지금까지의 합을 버리고 새로 시작하는경우
    if d[i][0] < d[i-1][0] + P[i]:
        d[i][0] = d[i-1][0] + P[i]
    # d[i][1] = 0
    # 0인 상태에서, 1로 들어오면서 ( 나를 제거하면서 ) 새로시작하는경우 ❌
    # 0인 상태에서, 1로 들어오면서 ( 나를 제거하면서 ) 잇는경우
    # 한번 제거한상태와 잇는 경우
    d[i][1] = max(d[i-1][0], d[i-1][1] + P[i])
print(d)
res = d[0][0]
for e in d:
    res = max([res] + e)
print(res)
