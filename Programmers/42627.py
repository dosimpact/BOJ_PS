

import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


Debug = True


def solution(jobs):
    jobsu = len(jobs)
    clock = 0
    diskQ = []
    heapq.heapify(diskQ)
    jobs.sort()
    res = 0
    # --------------------------
    while jobs or diskQ:
        # 현재 시간 안에 들어온 요청 큐에 넣기
        while jobs and clock >= jobs[0][0]:
            if Debug:
                print(f" enqu {jobs} | time {clock} | res {res}")
            t, a = jobs.pop(0)
            heapq.heappush(diskQ, (a, t))
        # 큐에서 하나 꺼내 실행
        if diskQ:
            a, t = heapq.heappop(diskQ)  # 3,0
            if Debug:
                print(f"process ..  amount { a} time {t}")
            res += (a) + (clock - t)
            clock += a
        else:
            clock += 1
        # 그렇지 않다면 시간 하나 흘려보내기
    return res // jobsu


print(solution(	[[0, 3], [1, 9], [2, 6]]))

"""
fb) 오잉 로직을 찍었는데 맞추었음....

그냥 직감적으로 >
특정 시간에 두개의 작업이들어왔어 > 가장 적은 시간내에 끝내는 작업먼저 처리하는게 개이득 
왜 어차피 

"""
