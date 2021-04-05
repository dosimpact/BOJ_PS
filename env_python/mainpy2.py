from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

# 처음에 보드 만들고
# 요청에 맞게, y증,X증,y감소,x감소 순으로 for문 돌린다.
graph = None


def printGraph():
    for row in graph:
        print(*row)
    print("-----")


def makeIterClockWise(sx, sy, ex, ey):
    # 포함,안포함
    iterlist = []
    for j in range(sy, ey):  # ->
        iterlist.append((sx, j))

    for i in range(sx, ex):  # down
        if i == sx:
            continue
        iterlist.append((i, ey - 1))

    for j in range(ey - 1, sy - 1, -1):  # <-
        if j == ey - 1:
            continue
        iterlist.append((ex - 1, j))

    for i in range(ex - 1, sx, -1):  # up
        if i == ex - 1:
            continue
        iterlist.append((i, sy))
    return iterlist


def swapClockwise(graph, sx, sy, ex, ey):
    iterlist = makeIterClockWise(sx - 1, sy - 1, ex, ey)
    log = []
    prev = graph[sx][sy - 1]
    for nx, ny in iterlist:
        log.append(graph[nx][ny])
        prev, graph[nx][ny] = graph[nx][ny], prev
    return min(log)


def solution(rows, columns, queries):
    global graph
    graph = []
    for r in range(rows):
        graph.append([(r) * (columns) + (1 + i) for i in range(columns)])
    # print(graph)
    ans = []
    for q in queries:
        ans.append(swapClockwise(graph, *q))
    return ans


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
