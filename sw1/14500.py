"""

E S M 

"""

import sys

Debug = False


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()


blocks = {0: [(0, 1), (0, 2), (0, 3)],
          1: [(1, 0), (2, 0), (3, 0)],
          2: [(0, 1), (1, 1), (1, 0)],
          3: [(0, 1), (-1, 1), (-2, 1)],
          4: [(1, 0), (2, 0), (2, 1)],
          5: [(0, 1), (1, 1), (2, 1)],
          6: [(-1, 0), (-2, 0), (-2, 1)],
          7: [(0, 1), (0, 2), (-1, 2)],
          8: [(1, 0), (1, 1), (1, 2)],
          9: [(0, 1), (0, 2), (1, 2)],
          10: [(-1, 0), (-1, 1), (-1, 2)],
          11: [(0, 1), (-1, 1), (-1, 2)],
          12: [(0, 1), (1, 1), (1, 2)],
          13: [(-1, 0), (-1, 1), (-2, 1)],
          14: [(1, 0), (1, 1), (2, 1)],
          15: [(0, -1), (0, 1), (1, 0)],
          16: [(0, -1), (0, 1), (-1, 0)],
          17: [(-1, 0), (1, 0), (0, 1)],
          18: [(-1, 0), (1, 0), (0, -1)]
          }


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dprint(graph)

ansMax = 0
for i in range(n):
    for j in range(m):
        for b in range(19):
            isposs = True
            ansTmp = graph[i][j]
            # 해당 좌표에서 , 블럭을 하나씩 노아보며 최댓값을 구한다.
            for (dx, dy) in blocks[b]:
                (nx, ny) = (i+dx, j+dy)
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    ansTmp += graph[nx][ny]
                else:
                    isposs = False
                    break
            if isposs:
                ansMax = max(ansMax, ansTmp)
print(ansMax)
"""
테트로미노 경우의 수 구할때

작은 프로그래밍 방법으로 구했다.

문제점은 : 연속된 블럭의 입력을 받겠끔 하는데 
법규 모양의 블럭은 그럴 수 없다..

"""
