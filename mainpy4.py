import sys
from copy import deepcopy


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

q = []  # 작업 큐
plist = [[10000, 0, 0, 1], [150000, 0, 0, 2], [100000, 0, 0, 3], [
    8000, 0, 0, 4], [7000, 0, 0, 5]]  # 실행 되어야 할 프로세스 시간 (ms) 대기시간, 종료된 시간
reslist = []
quantum = 5000  # CASE1. 퀀텀이 5s인 경우

clk = 0  # 전체 시간
qtimer = 0  # 퀀텀 타이머

q = deepcopy(plist)  # 작업큐에 모든 프로세스가 들어온다.
# ========================================================================init
print(f"작업 큐 : {q}")
while q:  # 작업큐가 없을때 까지.
    # 해당 ms에서 작업을 실행하고
    q[0][0] -= 1
    # 각 프로세스에 대한, 대기시간과 실행중인 프로세스작업을 업데이트
    for i in range(1, len(q), 1):
        q[i][1] += 1
    clk += 1
    qtimer += 1
    # 만약 작업이 종료되면 | 종료시간 적고,다음 작업 큐로 전환
    if q[0][0] <= 0:
        print(f"finish process at {clk}")
        q[0][2] = clk
        tmp = q.pop(0)
        reslist.append(tmp)
        continue
    # 퀀텀이 종료되면 | 다시 스케쥴링
    if qtimer >= quantum:
        tmp = q.pop(0)
        q.append(tmp)
        qtimer = 0
        print(f"swtich process at {clk}")
        continue
print(f"result : {reslist}")
