"""
https://programmers.co.kr/learn/courses/30/lessons/60058

 괄호가 개수는 맞지만 짝이 맞지 않은 형태로


'(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열
'('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열

균형 -> 올바른 변환



"""


# 빈 입력이라면 빈문자열 반환

import sys

sys.setrecursionlimit(10**6)
DEBUG = True


def isBlance(s: str):
    return s.count("(") == s.count(")")


def isCorrect(s: str):
    cnt = 0
    for se in s:
        if se == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False


def diver(s: str):
    # for i in range(0, len(s)):
    for i in range(0, len(s)+1):

        if s[:i] != "" and isBlance(s[:i]) and isBlance(s[i:]):
            if DEBUG:
                print("-->u ", s[:i], "-->v ", s[i:])
            return (s[:i], s[i:])
    print("ERROR!")


def go(s: str):
    #
    if DEBUG:
        print("--> s ", s)
        input()

    if s == "":
        return ""
    elif isCorrect(s):
        return s
    else:
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        u, v = diver(s)
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        if isCorrect(u):
            return u + go(v)
        else:  # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
            res = u[1:-1]
            tmp = list(res)
            i = 0
            j = len(tmp)-1
            while i < j:
                tmp[i], tmp[j] = tmp[j], tmp[i]
                i += 1
                j -= 1
            res = "".join(tmp)
            return '('+go(v)+')'+res


def solution(p):
    answer = go(p)
    return answer


print("res:", solution("()))((()"))
