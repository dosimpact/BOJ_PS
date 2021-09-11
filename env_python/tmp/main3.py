# 작업 - 중요도 순,
# 한 분류는 계속 한다. 도중에 새 작업 요청 들어오기 가능
# - 같은 작업이라면 이어서 처리
# 다른 분류 중 작업의 중요도가 높은것 선택 처리

# 처리한 분류번호의 순서는 ?
# 요청시각은 다 다르다.

# 자료 구조 딕셔너리
# 작업 이름 - (중요도,총작업시간, )


def solution(jobs):
    jobState = dict()
    jobs.sort(key=lambda x: (x[0]))
    print(jobs)
    # 작업을 정렬
    # 요청 시각 순으로 정렬 한다.
    nextEndTime = 0  # 작업종료시간
    result = []
    prevClass = None
    for job in jobs:
        # 요청 시각순으로 작업을 하나씩 꺼낸다.
        reqT, longT, classKey, priority = job  # 요청시간
        if nextEndTime <= reqT:
            # 이미 작업이 끝나 있다면 , 큐 작업을 진행시켜 본다.
            jobStateQ = jobState.values()
            jobStateQ.sort(key=lambda e: (e[0], e[2]))
            while nextEndTime <= reqT:
                # 큐 작업 후 nextEndTime 갱신
                prevP, prevT, prevClass = jobStateQ.pop()
                result.append(prevClass)
                nextEndTime += prevT
                pass
            # 현재 작업을 이어서 하는 경우 - 같은 클래스,
            if classKey == prevClass:
                result.append(prevClass)
                nextEndTime += prevT
            # 현재 작업을 큐에 넣는 경우,높은 우선 순위
            else:
                jobState[classKey][0] += priority
                jobState[classKey][1] += longT
        else:
            if classKey not in jobState:
                jobState[classKey] = [0, 0, classKey]
            jobState[classKey][0] += priority
            jobState[classKey][1] += longT
            pass
        # 2) 작업 종료시간 < 요청시간 - 바로 실행(우선순위 작업)
        # 3) 작업 종료시간 > 요청시간 - 작업 대기줄에 넣는다.

        # 가장 높은 중요도를 가진 작업을 관찰한다.
        pass
    return result


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [
      5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
