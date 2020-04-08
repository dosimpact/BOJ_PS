import sys


def input(): return sys.stdin.readline().rstrip()


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

canDown = []
for Col in zip(*graph):
    gidx = Col.index("#")
    try:
        midx = Col[::-1].index('X')
    except:
        midx = -1
    # print(f"{gidx},{midx}")
    if midx == -1:
        pass
    else:
        canDown.append(abs(gidx - (R-1 - midx))-1)
Down = min(canDown)
# 각 열을 돌면서, 각자. 공기가 몇개인지 센다. ( 반드시 땅은 존재, 운석은 없을수도)

# 최소 값만큼 운석을 떨군다.
if Down == 0:
    pass
else:
    for r in range(R-1, -1, -1):
        for c in range(C):
            if graph[r][c] == "X":
                graph[r][c] = "."
                graph[r+Down][c] = "X"

for g in graph:
    for e in g:
        print(e, end="")
    print()

"""

5 6
.XXXX.
...X..
......
#..###
######

9 7
XXX.XXX
X.XXX.X
X..X..X
X.....X
.......
.#...#.
.##.##.
.#####.
#######
"""
