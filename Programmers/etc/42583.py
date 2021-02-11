# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(blen, w, trucks):  # 다리 길이 / 총 무게 / 트럭들 무게
    sec = 0
    bridgeTrucks = []
    while True:
        # 트럭을 한칸씩 움직인다. | 0이 되버린 트럭은 제거 | 필터를 써서 제거함
        for e in bridgeTrucks:
            e[1] -= 1
        bridgeTrucks = list(filter(lambda x: x[1] > 0, bridgeTrucks))

        # 끝난경우 | 다리위 트럭 없음 | 더 갈 트럭도 없음.
        if len(trucks) == 0 and len(bridgeTrucks) == 0:
            break

        # 트럭을 하나 추가해 볼까? | 트럭스가 있고 | 그 트럭무게 + 다리위 트럭무게함 | 되면 넣기
        if len(trucks) > 0:
            weight = trucks[0]
            for e in bridgeTrucks:
                weight += e[0]
            if weight <= w:
                bridgeTrucks.append([trucks.pop(0), blen])
        sec += 1
    return sec+1


# 피드백 1 filter는 결과로 list가 아닌 filter 오브젝트를 반환한다.

# 피드백 2 꼭 논리를 작성하고 코드 짜기.!!
