from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(p, l):
    data = []
    for i, val in enumerate(p):
        if i == l:
            data.append([val, 1])
        else:
            data.append([val, 0])
    counter = 1
    maxval = max(data)  # 현재 최대값을 찾는다.

    while(True):
        now = data.pop(0)
        print(data, '<data now>', now, 'counter', counter)
        if now[0] == maxval[0]:
            if now[1] == 1:
                return counter
            counter += 1
            maxval = max(data)
        else:
            data.append(now)
    return 0


data = []
print(max(data))
