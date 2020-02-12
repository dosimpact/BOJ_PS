from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    return answer

# 파이썬 정렬하기 | 커스텀 정렬

# data.sort() 역시 정렬후, None반환 -> 원본이 훼손된다.

# sorted(리스트,reverse,key) 는 원본 훼손 없이 사용 가능


data = ['su', 'bed', 'app', 'king']

res = sorted(data)
print(res)  # ['bed', 'king', 'su']

res = sorted(data, reverse=True)
print(res)  # ['su', 'king', 'bed']

res = sorted(data, key=lambda x: len(x))  # 길이가 작은순
print(res)  # ['su', 'bed', 'app', 'king']

res = sorted(data, key=lambda x: (len(x), x))  # 길이가 작은순 + 사전순
print(res)  # ['su', 'app', 'bed', 'king']

res = sorted(data, key=lambda x: (len(x), x), reverse=True)  # 길이가 작은순 + 사전순
print(res)  # ['king', 'bed', 'app', 'su']
