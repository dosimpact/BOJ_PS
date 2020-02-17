# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(blen, w, trucks):  # 다리 길이 / 총 무게 / 트럭들 무게
    sec = 0
    now_trucks = []  # [ 트럭의 무게 , 남은 트럭의 거리]
    while True:
        if len(now_trucks) != 0:
            for i in range(len(now_trucks)):
                now_trucks[i][1] -= 1
        now_trucks = list(filter(lambda x: x[1] > 0, now_trucks))
        # 트럭이 다 건넌경우 중단,
        if len(trucks) == 0 and len(now_trucks) == 0:
            break
        # 남은 트럭이 있는경우 -> 현재 건너는중인 트럭 무게 + 건너려는 트럭 무게 합 이 w 이하라면 추가
        if(len(trucks) != 0):
            tmpWeight = trucks[0]
            for i in range(len(now_trucks)):
                tmpWeight += now_trucks[i][0]
            if tmpWeight <= w:
                now_trucks.append([trucks.pop(0), blen])
        sec += 1
    return sec + 1
