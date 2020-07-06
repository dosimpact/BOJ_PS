import math
#https://papercraft-blog.tistory.com/2
#0: min, 1: max
#피연산자 개수=>N//2+1
def solution(arr):
    N = len(arr)
    #d[i][j] = i번째 피연산자부터 j번째 피연산자까지 연산한 최대(1), 최소값(0)
    d = [[[_ for _ in range(2)] for _ in range(N//2+1)] for _ in range(N//2+1)]
    #d[0][0], d[1][1] 등 하나의 피연산자를 이용해 나올 수 있는 값을 초기값으로 세팅
    for i in range(N//2+1):
        d[i][i][0], d[i][i][1] = int(arr[i*2]), int(arr[i*2])
    #k는 d값 저장 순서 결정 => (1<= k <N//2+1) => 첫번째 반복은 피연산자 두 개로 만들 수 있는 값 저장, 두번째는 세 개로 만들 수 있는 값을 저장하도록 순서 조정
    for k in range(1,N//2+1):
        #각 피연산자 마다 반복
        for i in range(N//2+1):
            #인덱스 범위는 각 피연산자 마다 0~N//2 and 1~N//2 and 2~N//2 ... 
            if i+k < N//2+1:
                #min,max 계산 정확히 하기 위해 처음에 빈 d[i][i+k]에 엄청큰, 작은 값 세팅
                d[i][i+k][0], d[i][i+k][1] = math.inf, -9999999
                #현재 피연산자부터 i+k번째 피연산자 바로 전까지(나누는 기준이 되는 연산자 인덱스 고려)
                #if i =0, k=3: 1+2+3+4 => (1+2) + (3+4)
                for j in range(i, i+k):
                    if arr[j*2+1] == '+':
                        d[i][i+k][0] = min(d[i][i+k][0], d[i][j][0] + d[j+1][i+k][0])
                        d[i][i+k][1] = max(d[i][i+k][1], d[i][j][1] + d[j+1][i+k][1])
                    else:
                        #빼기 연산의 경우 (최대 = 최대 - 최소)이기 때문에 최소값도 저장해야함
                        d[i][i+k][0] = min(d[i][i+k][0], d[i][j][0] - d[j+1][i+k][1])
                        d[i][i+k][1] = max(d[i][i+k][1], d[i][j][1] - d[j+1][i+k][0])
    return d[0][N//2][1]
