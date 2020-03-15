"""

조사한 n분
터널안 차량의 수 m

0 - 1 : 2 3  1
1 - 2 : 2 3  0
2 - 3 : 4 1  3
"""


import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
counter = 0

for i in range(N-1, 0, -1):
    counter += 1
    if N % i == 0:
        break
print(counter)
