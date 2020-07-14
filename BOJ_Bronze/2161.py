import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

q = [i for i in range(1, N+1)]

while q:
    if len(q) == 1:
        print(q.pop(0), end=' ')
        break
    print(q.pop(0), end=' ')
    q.append(q.pop(0))

"""
0
1000
"""
