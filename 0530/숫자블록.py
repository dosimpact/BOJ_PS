
import sys


def input(): return sys.stdin.readline().rstrip()

# [ 1 ~ k //2 ] 중 가장 큰 소인수
# 1. 소인수를 찾아.
# 2. 그중 k//2 까지 max 를 골라.

# 개선. 1. dp


def one(k: int):
    if k == 1:
        return 0
    if k % 2 == 0:
        return k//2
    for i in range(k//2, 0, -1):
        if k % i == 0:
            return i
    return 1


def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(one(i))
    return answer
