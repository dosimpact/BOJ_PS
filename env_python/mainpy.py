

def solution(n: int):
    # 토스 체
    check = [-1 for i in range(0, n+1)]
    pc = 0  # 소수의 갯수
    pn = []  # 소수의 배열
    # -1 소수인것 체크.
    for i in range(2, n+1):  # 2...n 까지 검사
        if check[i] == -1:  # 소수임
            pc += 1
            pn.append(i)
            # 3*3 = 9 , 12 , 15 ... n까지 제거
            for j in range(i*i, n+1, i):  # 2*2 =4 ,6 8, ...,n 까지 제거
                check[j] = 1
    return pc


print(solution(1))
print(solution(2))
print(solution(5))  # 2 3  5
print(solution(10))
print(solution(1000))
