"""

"""
import sys


def input(): return sys.stdin.readline().rstrip()


check = [0 for _ in range(31)]
for _ in range(28):
    how = int(input())
    check[how] = 1

for i, c in enumerate(check):
    if i == 0:
        continue
    if c == 0:
        print(i)
