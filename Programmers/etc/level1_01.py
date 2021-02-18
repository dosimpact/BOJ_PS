from collections import deque
import sys

SIZE = 101


def input(): return sys.stdin.readline().rstrip()


def solution(s):
    answer = []
    # 문자열 길이만큼 1~len(s) for문 - i개로 쪼개서 배열을 만듬 -> 같은거를 비교하는 함수 -> 길이 저리
    for i in range(1, len(s)+1):
        var = []
        for j in range(0, len(s), i):  # j
            var.append(s[j: j+i])
        res = ""
        count = 1
        for i in range(len(var)-1):
            if(var[i] == var[i+1]):  # 같은경우라면  count증가
                count += 1
            else:  # 다른경우라면 문자열 만들어 주기 -> count 가 2이상부터 접두해서 붙여주기
                if count == 1:
                    res += var[i]
                else:
                    res += (str(count) + var[i])
                count = 1
        if count == 1:
            res += var[-1]
        else:
            res += (str(count) + var[-1])
        answer.append(len(res))
    return min(answer)


s = "xababcdcdababcdcd"
solution(s)
