
import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

"""
n 번째 피보나치 diver로 나눈것
"""
diver = 1234567

d = {}


def dp(n):
    if n <= 1:
        return n
    if n == 2:
        return 1
    else:
        if n in d:
            return d[n]
        d[n] = int((dp(n-1)+dp(n-2)) % diver)
        return d[n]


def solution(n):
    answer = dp(n)
    return answer


for i in range(100000):
    print(solution(i))
