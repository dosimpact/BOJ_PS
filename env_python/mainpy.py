
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬

# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

import collections
import itertools


def solution(strings, n):
    strings = sorted(strings, key=lambda x: (x[n], x))
    return strings


pool = ['a', 'b', 'c']

# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
print(list(itertools.permutations(pool)))

# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(list(map(lambda x: "".join(x), itertools.permutations(pool))))
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(list(map("".join, itertools.permutations(pool))))
