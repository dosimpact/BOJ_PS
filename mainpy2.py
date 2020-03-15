DEBUG = True


def solution(str1, str2):
    # 문자열 집합 2개를 만든다.
    A = [str1[i:i+2].upper()
         for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    B = [str2[i:i+2].upper()
         for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if DEBUG:
        print("-->1", A, B)
    # 공통의 원소들을 빼온다.
    comSet = set(A) | set(B)
    if DEBUG:
        print("-->2", comSet)
    AUB = []  # 합
    AVB = []  # 교
    # 공통의 원소를 돌면서, 합집합에서는 max를 이용하면 다 들어갈것이고, 교집합에서는 min을 이용하면 0은 알아서 빠지겠끔 만들어
    for com in comSet:
        AUB.extend([com]*(max(A.count(com), B.count(com))))
        AVB.extend([com]*(min(A.count(com), B.count(com))))
    if DEBUG:
        print("-->3", AUB, AVB)
    if AUB:
        return int((len(AVB)/len(AUB))*65536)
    else:
        return 65536


print(solution("++", "CD"))
