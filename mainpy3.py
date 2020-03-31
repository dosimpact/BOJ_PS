"""
https://www.acmicpc.net/problem/3024


 세 글자가 행, 열, 또는 대각선으로 연속할 때, 그 플레이어가 승리

"""

import sys


n = int(input())

graph = [list(input()) for _ in range(n)]


def isvaild(s: []):
    cnt = 0
    now = '.'
    for i in range(len(s)):
        # 점인경우는 무조건 초기화
        if s[i] == '.':
            cnt = 0
            now = s[i]
        # 현재와 일치하는경우
        if s[i] == now:
            cnt += 1
            if cnt == 3:
                return now
        # 현재와 다른 경우
        else:
            cnt = 1
            now = s[i]
    return ''


# 가로 검사


if n < 3:
    print('ongoin')
    exit(0)

for i in range(n):
    # 해당 대각선에서
    res = isvaild(graph[i])
    if res != '':
        print(res)
        exit(0)
    # 세로 검사
for j in range(n):
    # 해당 대각선에서
    record = []

    for i in range(0, n):
        record.append(graph[i][j])
    res = isvaild(record)
    if res != '':
        print(res)
        exit(0)

for i in range(0, n):
    record = []
    for j in range(0, n):
        if i >= 1 and j >= 1:
            continue
        (x, y) = (i, j)
        while (x >= 0 and y >= 0 and x < n and y < n):
            record.append(graph[x][y])
            x += 1
            y += 1
        res = isvaild(record)
        if res != '':
            print(res)
            exit(0)

for i in range(0, n):
    record = []
    for j in range(0, n):
        if i >= 1 and j < n-1:
            continue
        (x, y) = (i, j)
        while (x >= 0 and y >= 0 and x < n and y < n):
            record.append(graph[x][y])
            x += 1
            y -= 1
        res = isvaild(record)
        if res != '':
            print(res)
            exit(0)

print("ongoing")
"""

세 글자가

1개인 경우
다 .인경우


1
T

1
.
"""


"""
5
..A..
.A...
A....
.....
.....

5
.....
.....
.....
.....
.....

5
A.A..
.A...
A.A..
...A.
....B


5
A.AAA
.....
.....
.....
.....
"""
