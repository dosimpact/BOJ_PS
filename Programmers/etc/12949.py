def solution(A, B):
    C = []
    # 새로운 C행의 i,j 인덱서
    i = len(A)  # 행
    j = len(B[0])  # 열
    k = len(A[0])  # 곱하기 반복자
    for Ci in range(i):
        Crow = []
        for Cj in range(j):
            tmp = 0  # 한행에서 각 열마다 tmp를 만들거임
            for kit in range(k):
                tmp += A[Ci][kit]*B[kit][Cj]
            Crow.append(tmp)
        C.append(Crow)
    return C