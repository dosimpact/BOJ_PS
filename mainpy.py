from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


data = {}


def solution(participant, completion):
    answer = ''
    for e in participant:
        if e in data:
            data[e] += 1
        else:
            data[e] = 1
    for e in completion:
        data[e] -= 1
    for e in completion:
        if(data[e] == 1):
            answer = e
    return answer


s = "xababcdcdababcdcd"
solution(s)
