import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()

"""


"""

e, f, c = map(int, input().split())

ans = 0
e += f

while e >= c:
    # 한번 바꿔먹었을때
    res1, res2 = divmod(e, c)
    ans += res1
    e = res1 + res2
    #print(f"{res1} {res2} {e}")

print(ans)

"""
9 0 3
4

10 0 3
4

13 0 3
6

"""
