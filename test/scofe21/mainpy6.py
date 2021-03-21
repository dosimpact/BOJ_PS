import sys
import math
from collections import deque
input = sys.stdin.readline


# 한번에 한명만 입장
# 각 정사각형 곤간에 의류 셋팅 ( 무작위 숫자 만큼)
# 몇벌의 의류인지 지도, 입구 최상단외쪽, 출구 최하단 오른쪽
# 탐색 : 오른쪽or아래 - 이동한 경로의 모든 의류 바구니 - 90% 구매 가능

# 최대한 많은 옷을 구매,( 비싼 가격이 아닌 )


# 백트레킹 | X M 이 1만이나 되니까
# d(ij) = 옷의 수 , max(d(i-1,j), d(i,j-1)) + 1
M, N = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
d = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        d[i][j] = A[i][j]
        if i > 0:
            d[i][j] = max(d[i][j], d[i-1][j] + A[i][j])
        if j > 0:
            d[i][j] = max(d[i][j], d[i][j-1] + A[i][j])

print(d[N-1][M-1])

"""
3 5
3 4 5
2 3 9
3 9 3
4 5 1
1 3 6
"""
