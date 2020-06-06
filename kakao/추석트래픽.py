import sys
import re

timeinst = ["2016-09-15 01:00:04.002 2.0s"]


def TimetoInt(time: str):
    timeArr = time.split(" ")
    hms = list(map(int, timeArr[1].split(".")[0].split(':')))
    ms = int(timeArr[1].split(".")[1])
    interval = float(timeArr[2][:-1])*1000
    end = ms
    end += hms[2]*1000
    end += hms[1]*60*1000
    end += hms[0]*60*60*1000
    start = end - int(interval)
    print(start, end)
    return [start, end]


def solution(lines):
    vals = []
    stack_ptr = 0
    q = []  # 0 in , 1 out
    for line in lines:
        [start, end] = TimetoInt(line)
        q.append([start, 0])
        q.append([end+999, 1])
    # 정렬!!
    print(q)
    q.sort(key=lambda e: (e[0], -e[1]))
    print(q)
    for qe in q:
        if qe[1] == 0:
            stack_ptr += 1
        if qe[1] == 1:
            stack_ptr -= 1
        vals.append(stack_ptr)
    return max(vals)


print(solution(	["2016-09-15 01:00:04.001 2.0s",
                 "2016-09-15 01:00:07.000 2s"]))
"""
시간 1초에 [begin,end) 하는 점.
stack 에 interval 1초를 주는점
시간 1ms 초를 1000을 더하기 vs 999 더하기
"""
