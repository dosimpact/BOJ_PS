
import heapq
import sys

sys.setrecursionlimit(10**6)

Debug = True
# ------------------------------------------------------------------------------configure
SIZE = 370
PIVIOT = 160
N, M, T = map(int, input().split())
graph = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

# ------------------------------------------------------------------------------input
nt = 0
active_q = []
dactive_q = []
heapq.heapify(active_q)  # (활성시간,(w값)(좌표),)
heapq.heapify(dactive_q)
# ------------------------------------------------------------------------------ DS

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        graph[PIVIOT+i][PIVIOT+j] = row[j]
        if row[j] != 0:
            heapq.heappush(
                dactive_q, (graph[PIVIOT+i][PIVIOT+j]+nt, -graph[PIVIOT+i][PIVIOT+j], (PIVIOT + i, PIVIOT + j)))

if Debug:
    print("DEBUG")
    for i in range(N):
        for j in range(M):
            print(graph[PIVIOT+i][PIVIOT+j], end=" ")
        print()
if Debug:
    print("DEBUG")
    print(dactive_q)
"""
비활성 상태는 주어진 weight 동안 대기
활성 상태는 주어진 weight를 주변에 확장
cell 의 정보는 , 시간 오름차, 가중치 내림차, 좌표
"""
# t를 주어진 시간동안 돌려 |

# dactive에서 nt인 녀석들을 빼서 active로 진화

while nt > T:
    nt += 1  # 현재 시간 > 1시간 증가
    # active 번식
    while active_q[0][0] <= nt:
        cell = heapq.heappop(active_q)
    # dactive > active 화
    while dactive_q[0][0] <= nt:
        cell = heapq.heappop(dactive_q)
        # 시간 업데이트(현재시간 + weight), w,좌표는 그대로
        heapq.heappush(active_q, (nt+(-cell[1]), cell[1], cell[2]))
    pass

"""

2 2 10
1 1
0 2

5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2

"""
