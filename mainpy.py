def solution(number, k):
    answer = ''
    # 탐욕법 , 고를수 있는 unidx , upidx(포함) 을 정해서 가야함.
    jarisu = len(number) - k
    unidx = 0
    upidx = len(number) - jarisu
    #print(jarisu, unidx, upidx)
    check = [0 for _ in range(len(number))]
    for i in range(jarisu):
        # print(i)
        # 가능한 범위에서 최대값을 찾는다.
        tmp_max = -1
        tmp_j = 0
        for j in range(unidx, upidx+1):
            if check[j] == 0 and(tmp_max == -1 or tmp_max < int(number[j])):
                tmp_max = int(number[j])
                tmp_j = j
        # 값을 체크해주고, unidx를 좁혀서
        check[tmp_j] = 1
        unidx = tmp_j+1
        upidx += 1
        answer += str(tmp_max)

    return answer


print(solution("4177252841", 4))
"""
시간복잡도 특이점 걸린다.
N제곱 의 시간복잡도
"""
