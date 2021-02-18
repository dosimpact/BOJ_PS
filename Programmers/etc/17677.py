"""
https://programmers.co.kr/learn/courses/30/lessons/17677
 
자카드 유사도 집합 간의 유사도 == 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값

집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의
--

원소의 중복을 허용하는 다중집합 === 다중집합 B는 원소 1을 5개 가지고 있다고 하자. 이 다중집합의 교집합 A ∩ B는 원소 1을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 1을 max(3, 5)인 5개 가지게 된다. 



# st1 st2 => 다중집합의 원소
# 문자로 된 글자 쌍만 유효
# 대문자와 소문자의 차이는 무시 -> 하나로 변경
"""

DEBUG = False


def solution(str1, str2):
    if len(str1) == len(str2) == 0:
        return 65536
    answer = 0.25
    # st1 st2 => 다중집합의 원소
    if DEBUG:
        print("-->1", str1, str2)
    # 대문자와 소문자의 차이는 무시 -> 하나로 변경
    str1 = str1.upper()
    str2 = str2.upper()
    if DEBUG:
        print("-->2", str1, str2)
    # 문자로 된 글자 쌍만 유효
    A = []
    B = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i]+str2[i+1])
    if len(A) == len(B) == 0:
        return 65536
    if DEBUG:
        print("-->3", A, B)
    ASet = {}
    BSet = {}
    for a in A:
        if a in ASet:
            ASet[a] += 1
        else:
            ASet[a] = 1
    for b in B:
        if b in BSet:
            BSet[b] += 1
        else:
            BSet[b] = 1
    if DEBUG:
        print("-->4", ASet, BSet)
    AYBSet = {}  # 교집합
    AUBSet = {}  # 합집합
    # 합집합 처리 | 겹치는게 없으면 그냥 넣고 | 겹친다면 max 으로 넣고
    for _a in ASet:
        # 해당 키값이 B에도 있으면 max로 넣고 아니라면 그냥 넣어
        if _a in BSet:
            AUBSet[_a] = max([ASet[_a], BSet[_a]])
        else:
            AUBSet[_a] = ASet[_a]
        # 또 B를 도는데, 이미 들어간 경우라면 skip
    for _b in BSet:
        if _b in AUBSet:
            pass
        else:
            AUBSet[_b] = BSet[_b]
    if DEBUG:
        print("-->5", AUBSet)
    # 교집합 처리 | 겹치는게 없으면 그냥 넣고 | 겹친다면 min
    for _a in ASet:
        # 해당 키값이 B에도 있으면 max로 넣고 아니라면 그냥 넣어
        if _a in BSet:
            AYBSet[_a] = min([ASet[_a], BSet[_a]])
        # 또 B를 도는데, 이미 들어간 경우라면 skip
    if DEBUG:
        print("-->6", AYBSet)

    na, nb = (0, 0)
    for e in AYBSet:
        na += AYBSet[e]
    for e in AUBSet:
        nb += AUBSet[e]
    answer = na/nb
    return int(answer*65536)


print(solution("FRANCE", "french"))
