N, K = map(int, input().split())
item = []
for _ in range(N):
    w, v = map(int, input().split())
    item.append((w, v))

d = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):  # i번째 물건을 탐해본다.
    for j in range(1, K + 1):  # j 배낭의 무게로 시험
        if item[i - 1][0] > j:  # 담을 수 없음
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - item[i - 1][0]] + item[i - 1][1])

print(d[N][K])
"""
4 7
6 13
4 8
3 6
5 12
"""
