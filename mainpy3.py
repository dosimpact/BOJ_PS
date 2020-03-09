# 리팩토링 큰 수 만들기
def solution(number, k):
    AnsList = []

    # 모든 숫자들을 한바퀴씩 돌꺼야, AnsList에 들어가기전에 k만큼 청소
    for i in range(len(number)):
        while True:
            if AnsList and len(AnsList) > 0 and AnsList[-1] < number[i] and k > 0:
                k -= 1
                AnsList.pop()
            else:
                break
        AnsList.append(number[i])

        pass
    return "".join(AnsList[:len(number)-k])


print(solution("89", 1))
print(solution("98", 1))
