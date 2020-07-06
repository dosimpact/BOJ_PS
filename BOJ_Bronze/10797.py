"""
자동차 번호의 일의 자리 숫자와 날짜의 일의 자리 숫자가 일치
"""
# https://www.acmicpc.net/problem/10797
import sys


def input(): return sys.stdin.readline().rstrip()


n = int(input())
cars = list(map(int, input().split()))
# print(cars)
ans = 0
for car in cars:
    if car == n:
        ans += 1
print(ans)
