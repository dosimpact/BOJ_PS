
import sys


def input(): return sys.stdin.readline().rstrip()


data = [[1, 1], [2, 3]]
print(data)
for e in data:
    if e[1] == 1:
        data.pop(e)
print(data)
