
import sys
import math


def input(): return sys.stdin.readline().rstrip()


def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer += i
            if(i != int(n/i)):
                answer += int(n / i)
    return answer


print(solution(16))

"""
피드백:1)
math 임포트 -> 제곱근 구하는 함수 있다.

피드백 :2) 제곱근 까지만 시간복잡도를 가지고 
약수의 쌍을 구할 수 있지 않나
"""
