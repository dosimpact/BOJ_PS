 
from math import sqrt
def solution(begin, end):
    ans = [1 for _ in range(end-begin+1)]
    ans[0] = 0 if begin == 1 else 1
    
    for i in range(begin, end+1):
        #2 4 5 10 10 20 25 50
        #즉, 루트n이상의 수는 중복
        for j in range(2, int(sqrt(i))+1):
            #블록 넘버링 10000000까지 제한
            if i//j > 10000000:
                continue
            if i%j == 0:
                #나누어지는 두 수 중 가장 큰 수가 정답이기때문에 i//j
                #if j==2, i ==100이면 i//j = 50 
                ans[i-begin] = i//j
                #나누어 떨어졌다면 그 수가 가장 큰 수 <= 오름차순으로 나누고 있기 때문에
                break
    return ans
