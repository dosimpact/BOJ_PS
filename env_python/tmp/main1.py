K = None
COUNT = 0
STUDENT = None
COUNT_SET = set()
# 재귀 함수

# start부터 end까ㅏ지

# 이번에 start를 버린다,이번에 end를 포함시킨다.


def go(start, end, now_k):
    # k명의 재학생이 될때까지 end를 늘린다.
    if now_k < K:  # 0 , 1
        if end < len(STUDENT):
            # 재학생인경우 아닌경우, 더이상 늘릴수 없는 경우
            if STUDENT[end] == 1:
                return go(start, end+1, now_k+1)
            return go(start, end+1, now_k)
        return
    # k명의 재학생이 되었다면
    elif now_k == K:
        COUNT_SET.add((start, end))
    # cnt+=1
        if start <= end:
            if STUDENT[start] == 1:
                go(start+1, end, now_k-1)
            else:
                go(start+1, end, now_k)
        if end < len(STUDENT):
            if STUDENT[end] == 1:
                go(start, end+1, now_k+1)
            else:
                go(start, end+1, now_k)
    # call : start - 1 줄이는 경우
    # call : end + 1 늘리는 경우

    pass


def solution(student, k):
    global K, STUDENT
    K = k
    STUDENT = student
    go(0, 0, 0)
    return len(COUNT_SET)


print(solution([0, 1, 0, 0]	, 1))
