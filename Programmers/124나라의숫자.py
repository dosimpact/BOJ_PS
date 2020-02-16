
# https://www.acmicpc.net/problem/3101
import sys


def input(): return sys.stdin.readline().rstrip()

'''
n = 38
현재 n을 -3 , -9 , 27 을 최대한 해봐
-27 까지 성공해서 jari 변수가 3이야

그럼 9 로 나눈 몫과 나머지
그럼 3으로 나눈 몫과 나머지 구해 
'''


def solution(n):
    n = n-1
    answer = ''
    jari = 1  # 현재 한자리
    weight = 3
    while(True):
        if weight <= n:
            n = n - weight
            weight = weight*3
            jari += 1
        else:
            break
    # print(n, jari, weight)  # 26 3 27
    ans = []
    weight = weight/3  # 9
    # n을 weight로
    while(weight >= 3):
        tmpAns_, n = divmod(n, weight)  # 2 8
        weight /= 3
        ans.append(int(tmpAns_))
    ans.append(int(n))
    ans = list(map(lambda x: 1 if x == 0 else (2 if x == 1 else 4), ans))
    # print(ans)
    for e in ans:
        answer += str(e)
    print(answer)
    return answer


solution(1)
solution(2)
solution(3)
solution(4)
solution(8)
solution(11)
solution(12)
solution(38)
