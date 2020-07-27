
import sys
# https://www.acmicpc.net/problem/1463
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def go(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n-1) + 1
    if n % 2 == 0:
        temp = go(n//2) + 1  # 나누기(/)로 하면 소수 나와서 오류생김
        if d[n] > temp:
            d[n] = temp
    if n % 3 == 0:
        temp = go(n//3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


n = int(input())
d = [0]*(n+1)
print(go(n))
