import sys
from copy import deepcopy


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

q = []  # 작업 큐
# [ 프로세스 시간 (ms), 대기시간, 종료된 시간, pid,프로세스 시간]
plist = [[10000, 0, 0, 1, 10000], [15000, 0, 0, 2, 15000], [10000, 0, 0, 3, 10000], [
    8000, 0, 0, 4, 8000], [7000, 0, 0, 5, 7000]]
reslist = []
quantum = 10  # CASE1. 퀀텀이 5s인 경우

clk = 0  # 전체 시간
qtimer = 0  # 퀀텀 타이머
switchCnt = 0

q = deepcopy(plist)  # 작업큐에 모든 프로세스가 들어온다.
# ========================================================================init
print(f"작업 큐 : {q}")
print(f"time quantum is {quantum}ms")
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
        q[0][2] = clk
        tmp = q.pop(0)
        reslist.append(tmp)
        qtimer = 0

        continue
    # 퀀텀이 종료되면 | 다시 스케쥴링
    if qtimer >= quantum:
        tmp = q.pop(0)
        q.append(tmp)
        qtimer = 0
        switchCnt += 1
        continue
# print(f"result : {reslist}")
total_wating_time = sum(map(lambda e: e[1], reslist))
total_process_time = sum(map(lambda e: e[4], reslist))
total_response_time = sum(map(lambda e: e[2], reslist))

print(f"total waiting time |\t {total_wating_time}ms")
print(f"total processTime  |\t {total_process_time}ms")
print(f"total responseTime |\t {total_response_time}ms")
print(f"total switch count |\t {switchCnt}")

wsum = 0
for i in range(len(reslist)):
    pid = reslist[i][3]
    pt = reslist[i][4]
    rt = reslist[i][2]
    wt = reslist[i][1]

    rw = round(reslist[i][2]/total_response_time, 2)
    pw = round(reslist[i][4]/total_process_time, 2)
    print(f"{pid} processTime:{pt}({pw}) | responseTime:{rt}({rw})| waitingTIme:{wt}")
    print(f">>> weight:{round(abs(rw-pw),5)}")
    wsum += round(abs(rw-pw), 5)
print(f"wegith sum :{wsum}")
