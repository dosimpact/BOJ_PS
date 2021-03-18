import math
from collections import deque

# 주사위 조작 가능
# 보드판 10*10 -  1~100까지 수 순서대로
# 주사위 수만큼 이동, 100번 넘어가면 불가,
# 뱀 , 사다리 만나면 이동 , 시작,끝점은 연관 X + chaing 없음
# 최소 주사위 굴리는 횟수

# BFS + 백트래킹
# 0으로 이동 = 사다리 or 뱀
# 1로 이동 = 주사위
# 뒤로가는 경우가 이득인 상황 = 사다리 타기위한 뱀타기
# BFS이동이므로, check_q로 루프 제거
# ❌ 뱀과 사다리면 반드시 타야한다.

N, M = map(int, input().split())
quick = [0 for _ in range(101)]
check_q = [False for _ in range(101)]  # 퀵에 대한
check = [-1 for _ in range(101)]  # 노드 에 대한
for _ in range(N + M):
    u, v = map(int, input().split())
    quick[u] = v

dq = deque()
dq.append(1)  # 위치 1, 0번 주사위 굴림
check[1] = 0
while dq:
    x = dq.popleft()
    if quick[x] != 0:
        check[quick[x]] = check[x]
        x = quick[x]
    for dx in [1, 2, 3, 4, 5, 6]:
        nx = x + dx
        if nx > 100:
            continue
        if check[nx] != -1:
            continue
        check[nx] = check[x]+1
        dq.append(nx)
print(check[100])

"""
1 1
1 2
4 3
>17


2 1
2 50
31 99
51 30
>4

❌ 틀렸습니다. TC 발견 실패
- 문제 독해, 뱀과 사다리는 선택적으로 못타고 무조건 타야함..
"""
