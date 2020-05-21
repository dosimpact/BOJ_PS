import sys
from copy import deepcopy


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

q = []  # 작업 큐
plist = [[30000, 0, 0, 1, 30000], [15000, 0, 0, 2, 15000], [10000, 0, 0, 3, 10000], [
    8000, 0, 0, 4, 8000], [5000, 0, 0, 5, 5000]]  # 실행 되어야 할 프로세스 시간 (ms) 대기시간, 종료된 시간
reslist = []
quantum = 10  # CASE1. 퀀텀이 5s인 경우

clk = 0  # 전체 시간
qtimer = 0  # 퀀텀 타이머
switchCnt = 0

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

for i in range(len(reslist)):
    print(
        f"ps{reslist[i][3]} |\t processTime : {reslist[i][4]}ms|\t responseTime : {reslist[i][2]}ms|\t waitingTime : {reslist[i][1]}ms")

print(f"total waiting time |\t {sum(map(lambda e: e[1],reslist))}ms")
print(f"total switch count |\t {switchCnt}")
"""
quantum = 15000 
ps1 |    processTime : 10000ms|  responseTime : 10000ms|         waitingTime : 0ms
ps2 |    processTime : 15000ms|  responseTime : 25000ms|         waitingTime : 10000ms
ps3 |    processTime : 10000ms|  responseTime : 35000ms|         waitingTime : 25000ms
ps4 |    processTime : 8000ms|   responseTime : 43000ms|         waitingTime : 35000ms
ps5 |    processTime : 7000ms|   responseTime : 50000ms|         waitingTime : 43000ms
total waiting time |     113000ms


quantum = 5000 
ps1 |    processTime : 10000ms|  responseTime : 30000ms|         waitingTime : 20000ms
ps3 |    processTime : 10000ms|  responseTime : 40000ms|         waitingTime : 30000ms
ps4 |    processTime : 8000ms|   responseTime : 43000ms|         waitingTime : 35000ms
ps5 |    processTime : 7000ms|   responseTime : 45000ms|         waitingTime : 38000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     158000ms

quantum = 1000 
ps5 |    processTime : 7000ms|   responseTime : 35000ms|         waitingTime : 28000ms
ps4 |    processTime : 8000ms|   responseTime : 39000ms|         waitingTime : 31000ms
ps1 |    processTime : 10000ms|  responseTime : 43000ms|         waitingTime : 33000ms
ps3 |    processTime : 10000ms|  responseTime : 45000ms|         waitingTime : 35000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     162000ms

quantum = 10 
ps5 |    processTime : 7000ms|   responseTime : 35000ms|         waitingTime : 28000ms
ps4 |    processTime : 8000ms|   responseTime : 39000ms|         waitingTime : 31000ms
ps1 |    processTime : 10000ms|  responseTime : 44980ms|         waitingTime : 34980ms
ps3 |    processTime : 10000ms|  responseTime : 45000ms|         waitingTime : 35000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     163980ms
"""
