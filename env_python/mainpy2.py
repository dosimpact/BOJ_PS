import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(2)]  # [위,아래][i번째]
    d = [[0 for _ in range(0, 3)] for _ in range(N + 1)]

    d[1][0] = 0  # 안ㄸ드
    d[1][1] = P[0][0]  # 위뜯
    d[1][2] = P[1][0]  # 아래 뜯

    for i in range(2, N + 1):
        d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])  # 스티커를 안뜯는 경우
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + P[0][i-1]  # 위에를 뜯는경우
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + P[1][i-1]  # 아랠르 뜯는 경우
    print(max(d[N]))
