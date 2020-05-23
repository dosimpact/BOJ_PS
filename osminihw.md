# osminihw

```python
import sys
from copy import deepcopy


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

q = []  # 작업 큐
plist = [[10000, 0, 0, 1, 10000], [15000, 0, 0, 2, 15000], [10000, 0, 0, 3, 10000], [
    8000, 0, 0, 4, 8000], [7000, 0, 0, 5, 7000]]  # 실행 되어야 할 프로세스 시간 (ms) 대기시간, 종료된 시간
reslist = []
quantum = 5000  # CASE1. 퀀텀이 5s인 경우

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

```

# 결론

```js
- Case1) time quantum is 5s

time quantum is 5000ms
ps1 |    processTime : 10000ms|  responseTime : 30000ms|         waitingTime : 20000ms
ps3 |    processTime : 10000ms|  responseTime : 40000ms|         waitingTime : 30000ms
ps4 |    processTime : 8000ms|   responseTime : 43000ms|         waitingTime : 35000ms
ps5 |    processTime : 7000ms|   responseTime : 45000ms|         waitingTime : 38000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     158000ms
total switch count |     6


- Case2) time quantum is 1s

time quantum is 1000ms
ps5 |    processTime : 7000ms|   responseTime : 35000ms|         waitingTime : 28000ms
ps4 |    processTime : 8000ms|   responseTime : 39000ms|         waitingTime : 31000ms
ps1 |    processTime : 10000ms|  responseTime : 43000ms|         waitingTime : 33000ms
ps3 |    processTime : 10000ms|  responseTime : 45000ms|         waitingTime : 35000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     162000ms
total switch count |     45

- Case3) time quantum is 10ms

time quantum is 10ms
ps5 |    processTime : 7000ms|   responseTime : 35000ms|         waitingTime : 28000ms
ps4 |    processTime : 8000ms|   responseTime : 39000ms|         waitingTime : 31000ms
ps1 |    processTime : 10000ms|  responseTime : 44980ms|         waitingTime : 34980ms
ps3 |    processTime : 10000ms|  responseTime : 45000ms|         waitingTime : 35000ms
ps2 |    processTime : 15000ms|  responseTime : 50000ms|         waitingTime : 35000ms
total waiting time |     163980ms
total switch count |     4995


타임퀀텀이 줄수록 프로그램의 최초 실행까지의 시간은 줄어들지만
전체적인 waiting  time이 늘어났습니다.
반대로 타임퀀텀이 클수록 하나의 프로세스의 응답시간이 줄어들었습니다.

변수 : TimeQuamtum
processTime  + waitingTime = responseTime
- 문제: 프로세스 타임이 긴 프로세스들 때문에 전반적인 waitingtime이 늘어남.
- 문제: 그렇다고, 프로세스 타임이 짧은 프로세스들만 실행 시키면, 긴 프로세스들은 responeTime이 늦어진다.


fairness을 측정하기 위한 좋은 방법.

긴 프로세스는 긴 응답시간을 가지고, 짧은 프로세스는 짧은 응답시간을 가지는것이 공평합니다.
그래서 프로세스별로 시간적 비율을 구했습니다.
p1 p2 프로세스가 각각 10, 90 러닝 타임이라면 0.1 0.9 의 비율을 갖고
p1 p2 프로세스가 실제 응답한 시간비율은 0.2 0.8 이라면
p1 는 적은 프로세스 타임임에도 긴 응답시간을 가진것이고
p2 는 긴 프로세스 타임 임에도 짧은 응답시간을 가졌다고 봅니다.

그래서 두개의 비율의 차이가 적을수록, 공평하게 프로세스 길이에 따라서 응답했다고 봅니다.

실험 결과:

- case1, 퀀텀 5000ms

time quantum is 5000ms
total waiting time |     158000ms
total processTime  |     50000ms
total responseTime |     208000ms
total switch count |     6
1 processTime:10000(0.2) | responseTime:30000(0.14)| waitingTIme:20000
>>> weight:0.06
3 processTime:10000(0.2) | responseTime:40000(0.19)| waitingTIme:30000
>>> weight:0.01
4 processTime:8000(0.16) | responseTime:43000(0.21)| waitingTIme:35000
>>> weight:0.05
5 processTime:7000(0.14) | responseTime:45000(0.22)| waitingTIme:38000
>>> weight:0.08
2 processTime:15000(0.3) | responseTime:50000(0.24)| waitingTIme:35000
>>> weight:0.06
wegith sum :0.26

- case2, 퀀텀 1000ms

time quantum is 1000ms
total waiting time |     162000ms
total processTime  |     50000ms
total responseTime |     212000ms
total switch count |     45
5 processTime:7000(0.14) | responseTime:35000(0.17)| waitingTIme:28000
>>> weight:0.03
4 processTime:8000(0.16) | responseTime:39000(0.18)| waitingTIme:31000
>>> weight:0.02
1 processTime:10000(0.2) | responseTime:43000(0.2)| waitingTIme:33000
>>> weight:0.0
3 processTime:10000(0.2) | responseTime:45000(0.21)| waitingTIme:35000
>>> weight:0.01
2 processTime:15000(0.3) | responseTime:50000(0.24)| waitingTIme:35000
>>> weight:0.06
wegith sum :0.12


- case2, 퀀텀 10ms


time quantum is 10ms
total waiting time |     163980ms
total processTime  |     50000ms
total responseTime |     213980ms
total switch count |     4995
5 processTime:7000(0.14) | responseTime:35000(0.16)| waitingTIme:28000
>>> weight:0.02
4 processTime:8000(0.16) | responseTime:39000(0.18)| waitingTIme:31000
>>> weight:0.02
1 processTime:10000(0.2) | responseTime:44980(0.21)| waitingTIme:34980
>>> weight:0.01
3 processTime:10000(0.2) | responseTime:45000(0.21)| waitingTIme:35000
>>> weight:0.01
2 processTime:15000(0.3) | responseTime:50000(0.23)| waitingTIme:35000
>>> weight:0.07
wegith sum :0.13

결과 :

퀀텀 : 5000ms > 1000ms > 10ms
공평성 : 0.26  > 0.12 < 0.13

퀀텀이 1000ms 일때, 공평성 0.12 로 가장 fairness 했다고 생각합니다.




```
