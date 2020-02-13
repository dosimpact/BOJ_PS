from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(progresses, speeds):
    comdate = [0]*len(progresses)
    answer = []
    # for문을 1->100(일)번 돌리면서 progresses를 각 속도 마다 증가 시킨다. 각 일수를 체크하여 최초 배포일을 넣어준다.
    for i in range(1, 101):
        for j in range(0, len(progresses)):
            isbapo = False
            progresses[j] += speeds[j]
            if(progresses[j] >= 100 and comdate[j] == 0 and not isbapo):
                comdate[j] = i  # 완료했어, 출력하거나, 스택에 넣거나.
                isbapo = True

    res = comdate
    while(len(res) > 0):
        now = res[0]
        filtered = list(filter(lambda x: x > now, res))
        answer.append(len(res) - len(filtered))
        res = filtered

    return answer


'''
작업을 100일동안 돌려보면서, 각 작업을 스피드 만큼 증가시킵니다. 해당 작업량이 100이 넘어가면
i일을 해당 작업 리스트에 등록
각 작업 예상 결과일 리스트를 반환

앞에서부터 
'''
