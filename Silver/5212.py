
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]

Ngraph = [['.' for _ in range(C+2)] for _ in range(R+2)]
# 바다를 하나씩 더 늘리자.
for i in range(R):
    for j in range(C):
        Ngraph[i+1][j+1] = graph[i][j]


# 섬제거
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
willremove = []

for i in range(R+2):
    for j in range(C+2):
        if Ngraph[i][j] == "X":
            cnt = 0
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if Ngraph[nx][ny] == '.':
                    cnt += 1
            if cnt >= 3:
                willremove.append((i, j))

for i, j in willremove:
    Ngraph[i][j] = '.'


# 위아래 바다 제거 (애러) > 위아래 바다가 아닌, 그냥 한줄이 바다인거 다 제거됨.
# i = 0
# while True:
#     if Ngraph[i].count('.') == C+2:
#         Ngraph.pop(i)
#         i = 0
#         continue
#     i += 1
#     if i >= len(Ngraph):
#         break
# for Ng in Ngraph:
#     print(*Ng)
# for Ng in Ngraph:
#     print(*Ng)

SR, ER, SC, EC = 0, R+1, 0, C+1

for Ng in Ngraph:
    if Ng.count('.') == C+2:
        SR += 1
    else:
        break

for Ng in Ngraph[::-1]:
    if Ng.count('.') == C+2:
        ER -= 1
    else:
        break

# print(SR, ER)

for Ng in zip(*Ngraph):
    if Ng.count('.') == R+2:
        SC += 1
    else:
        break

for Ng in list(zip(*Ngraph))[::-1]:
    # print(f"DEBUG {Ng}")
    if Ng.count('.') == R+2:
        # print(f"DEBUG EC{EC}")
        EC -= 1
    else:
        break

# print(SC, EC)

for i in range(SR, ER+1):
    for j in range(SC, EC+1):
        print(Ngraph[i][j], end="")
    print()


"""
3 10
..........
..XXX.XXX.
XXX.......

3 12
............
...XXX.XXX..
.XXX........


4 12
............
..XXX.XXX.X.
............
XXX.........

"""
