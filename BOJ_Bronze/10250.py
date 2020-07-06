import sys


def input(): return sys.stdin.readline().rstrip()


"""
2 // T
6 12 10 // H W N
30 50 72 // H W N
"""

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    u, v = divmod(n-1, h)  # w와 h 층수가 나온다.
    res = str(v+1)+str(u+1).rjust(2, '0')  # hw 호 로 표현
    print(res)
