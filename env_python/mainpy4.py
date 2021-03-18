import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# NN 물고기 M마리, 아기상어 1마리
# 한칸에 최대 1마리, 물고기는 크기가 있다.
# 아기상어는 2 크기, 1초에 4방향 이동
# 자기 보다 큰 물고기 있으면 이동 불가
# 자기 보다 작은 물고기 먹음, + 이동 > 자산의 크기 = 같은 수의 물고기
# 크기 2면 , 2마리 먹어야 3됨
# 자기 동일한 물고기 이동만 가능

# 먹을 수 있는 물고기
# 가장 위, 가장 왼쪽 먼저 먹는다.
# 물고기를 잡아먹을 수 있는 시간

fished = None  # 물고기 크기별 위치
# BFS 후 작은 물고기에 갈 수 있으면
dist = None  # 각 작은 물고기의 거리 *물고기 성장시 다시 업뎃해야함

while True:
    # 더이상 먹을 수 없는 경우

    #


"""
// 큰 크기의 물고기에 갇힘

5
0 0 0 0 1
0 2 2 2 2
1 0 0 0 0
2 2 2 2 0
9 0 0 0 0

5
0 0 0 0 1
0 3 3 3 3
0 0 0 0 1
3 3 3 3 0
9 0 0 0 0

"""
