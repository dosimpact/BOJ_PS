def solution(number, k):
    AnsList = []
    # 일딴 넘버들을 정답 리스트에 넣는다. 첫자리수가 가장 크게끔 k번 앞에 수를 뺄 수 있다.

    for i, num in enumerate(number):
        fb) 다 만들었는데 계속 넣잖아!!!
        if len(AnsList) == len(number) - k:
            break
        AnsList.append(num)
        while(True):
            if len(AnsList) > 1 and AnsList[-1] > AnsList[-2] and k > 0:
                AnsList.pop(-2)
                k -= 1
            else:
                break
        # AnsList에 일딴 넣어.
        print(AnsList, k)
    return "".join(AnsList[:len(number) - k])


print(solution("89", 1))
print(solution("98", 1))
