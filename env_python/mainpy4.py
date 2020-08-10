import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


T = int(input())  # 6
P = [0 for _ in range(T+1)]  # [i번째 포도주]
for _ in range(1, T + 1):
    P[_] = int(input())

# [i번째 포도주 까지][j번 연속 먹은경우] 최대로 마신양
D = [[0 for _ in range(3)] for _ in range(T + 1)]
D[1][0] = 0
D[1][1] = P[1]
D[1][2] = 0
for i in range(2, T+1):
    D[i][0] = max(D[i-1][0], D[i-1][1], D[i-1][2])
    D[i][1] = D[i-1][0] + P[i]
    D[i][2] = D[i - 1][1] + P[i]
print(max(D[T]))
