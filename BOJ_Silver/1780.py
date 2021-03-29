from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# 종이의 갯수 -   3등분해서 각각 자른다.
# 같은 종이로만 이뤄지면
# 3**14 < 3**16 < 1초
ans_counter = [0, 0, 0]  # -1,0,1
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def same(x, y, x_span, y_span):
    ref = graph[x][y]
    for nx in range(x, x + x_span):
        for ny in range(y, y + y_span):
            if ref != graph[nx][ny]:
                return None
    return ref


def go(x: int, y: int, x_span: int, y_span: int):
    # base case - 1
    if x_span == 1 and y_span == 1:
        ans_counter[graph[x][y] + 1] += 1
        return
    res = same(x, y, x_span, y_span)
    # ❌ 타입 주의 0 은 False
    if res != None:  # base case - all same
        ans_counter[res + 1] += 1
        return
    else:
        for i in range(x, x + x_span, x_span // 3):
            for j in range(y, y + y_span, y_span // 3):
                go(i, j, x_span // 3, y_span // 3)


go(0, 0, N, N)

for i in range(len(ans_counter)):
    print(ans_counter[i])


"""
1
1
"""