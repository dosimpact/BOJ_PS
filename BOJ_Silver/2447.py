import sys


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

graph = None


def rec(x: int, y: int, w: int):
    global graph
    if w == 1:
        graph[x][y] = "*"
        return

    for i in range(x, x+w, w//3):  # 0 9 18
        for j in range(y, y+w, w//3):
            if i == x+w//3 and j == y+w//3:
                continue
            #print(f">{w} : {i}, {j} ")
            rec(i, j, w//3)


N = int(input())
graph = [[" " for _ in range(N)] for _ in range(N)]
rec(0, 0, N)

for g in graph:
    for e in g:
        print(e, end="")
    print()
