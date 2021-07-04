from sys import stdin, setrecursionlimit
from collections import deque, defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


# 4,7 만 이뤄진 수, 범위 갯수
A, B = map(int, input().split())
ans = 0


def go(x: int):
    global ans
    if x > B:
        return
    if A <= x and x <= B:
        ans += 1
    go(x*10 + 4)
    go(x*10 + 7)


go(0)
print(ans)
