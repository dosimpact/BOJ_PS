
import sys


def input(): return sys.stdin.readline().rstrip()


obj = [-1 for _ in range(5001)]
s = int(input())

for b in range(0, 1668):
    for a in range(0, 1001):
        now = (5*a)+(3*b)
        if now <= 5000 and obj[now] == -1:
            obj[now] = (a+b)

print(obj[s])
