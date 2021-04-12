from sys import stdin, setrecursionlimit
from collections import deque, defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)
# 벨트화 로봇이 함께 움직여야함, 로봇 올라간 순서 알아야함

N, K = map(int, input().split())
# (내구도,로봇여부)
belt = deque(map(lambda x: [int(x), 0], input().split()))
robots = []  # 로봇 움직임 우선순위, 인덱스
cycle = 0
upIdx, downIdx = 0, N - 1

while True:
    print(f"cycle,upIdx,downIdx {cycle,upIdx,downIdx}")
    print(belt, robots)
    # 한칸 회전
    cycle += 1
    upIdx, downIdx = (upIdx - 1) % len(belt), (downIdx - 1) % len(belt)
    # 내려가는 위치 내리기
    if belt[downIdx][1] != 0:  #
        belt[downIdx][1] -= 1
        robots.remove(downIdx)

    # 벨트 위 로봇 이동
    for i, ridx in enumerate(robots):
        nidx = (ridx + 1) % len(belt)
        if belt[nidx][0] > 0 and belt[nidx][1] != 0:  # 내구도 0이상,로봇없음
            # 밸트 - 로봇 이동, 내구도 처리
            belt[ridx][1] -= 1
            belt[nidx][0] -= 1
            belt[nidx][1] += 1
            # 우선순위 메타 데이터 수정
            robots[i] = nidx

    # 올라가는 위치 올리기 - 내구도 가능시
    if belt[upIdx][0] > 0 and belt[upIdx][1] == 0:
        belt[upIdx][0] -= 1
        belt[upIdx][1] += 1
        robots.append(upIdx)  # 해당 idx 다음 순서임

    # 종료조건

    if len(list(filter(lambda x: x[0] == 0, belt))) >= K:
        break
    print(f"cycle,upIdx,downIdx {cycle,upIdx,downIdx}")
    print(belt, robots)
    input()
print(cycle)
"""
200*1000 = 2(10**5)(10**2)

3 2
1 2 1 2 1 2
0   2 = ( N-1 ) ( <-- 이동 )

문제 : 로봇의 우선순위를 알아서, 밸트위 로봇에 참조해야함
1) 밸트 이동시
2) 로봇 이동시 > 우선순위 belt idx update

벨트 고정, 포인터 <-- , 로봇 --> 
로봇 자체 움직임만 +=1

"""