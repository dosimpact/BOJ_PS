
import sys
import math


def input(): return sys.stdin.readline().rstrip()


# 문자열을 파싱 -> 숫자가 나오면 idx를 하나 늘린다.
def solution(dartResult):
    result = []
    idx = 0
    tmpScore = ''
    for dart in (dartResult):
        # 숫자인 경우 | 해당 숫자 push 및 idx++
        if dart >= '0' and dart <= '9':
            tmpScore += dart
        # S D T 인경우  | 해당 숫자 제곱,세제곱
        if dart in ['S', 'D', 'T']:
            idx += 1
            result.append(int(tmpScore))
            tmpScore = ''
            if dart == 'S':
                pass
            elif dart == 'D':
                result[idx - 1] = result[idx-1]**2
            elif dart == 'T':
                result[idx - 1] = result[idx-1]**3
        # *이나 #인 경우 ( 보나스 ) | 해당 인덱스에서 처리  ( 예외처리 필수)
        if dart == '#':
            result[idx - 1] = -result[idx-1]
        if dart == '*':
            result[idx - 1] = result[idx-1]*2
            if(idx - 2 >= 0):
                result[idx-2] = result[idx-2]*2
    return sum(result)


print(solution("1D2S#10S"))

"""
다트 3번 던진다. -> 0~10점 ->
영역 : s,d,t 제곱 해서 줌
추가옵션 : 
스타상 : 전 점수 + 이번 점수 각 2배로 만듬 ( 처음나오는경우 첫점수만) | 중첩기능
아차상 : 해당 점수를 마이너스 | 스타상 중첩기능 -2배 |


"""
