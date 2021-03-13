
from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 대규모 토지 개발
# NN 토지, N은 2,4 ... 32
# 각 칸에는 토지개발 이익이 있음
# 개발로 얻을 수 있는 이익중 최댓값
# 하나의 칸이 남으면 개발 종료 -

# d 2승번째 개발할대 최대 이익

N, maxAns = None, []
graph = None

# 현재 중심 x,y - 범위 dx,dy, 가치 v


def go(sx: int, sy: int, ex: int, ey: int, v: int):
    global maxAns
    if sx == ex or sy == ey:
        maxAns.append(v)
        return
    # print(f" sx,ex,sy,ey {sx,ex,sy,ey}")
    # go(sx, sy, ex, ey, v)
    midx, midy = (sx+ex)//2, (sy+ey)//2
    if ex != midx:
        p = max(graph[i][j] for i in (sx, midx) for j in (sy, ey))
        go(sx, sy, midx, ey, v+p)  # 이쪽 개발을 안했다.
    if sx != midx:
        p = max(graph[i][j] for i in (midx, ex) for j in (sy, ey))
        go(midx, sy, ex, ey, v+p)
    if ey != midy:
        p = max(graph[i][j] for i in (sx, ex) for j in (sy, midy))
        go(sx, sy, ex, midy, v+p)
    if sy != midy:
        p = max(graph[i][j] for i in (sx, ex) for j in (midy, ey))
        go(sx, midy, ex, ey, v+p)


def main():
    global graph, N
    N = int(input())  # 4
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    go(0, 0, N-1, N-1, 0)
    print()
    print(max(maxAns))


if __name__ == "__main__":
    main()


"""
4
1 3 4 5
6 2 9 9
4 3 10 5
5 2 8 6
>34
"""
# DP로 풀릴것같아서 고민하다 BFS완전탐색으로 가려다가 디버깅 실패
