"""
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지

가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이

색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이

색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다
"""

# https://www.acmicpc.net/problem/2563

import sys


def input(): return sys.stdin.readline().rstrip()


board = [[0 for _ in range(100)] for _ in range(100)]
su = int(input())

for _ in range(su):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

ans = 0
for b in board:
    ans += b.count(1)
print(ans)
