
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(routes):
    global check, meta
    routes.sort()
    stack = []
    ans = 0
    for i, [sidx, eidx] in enumerate(routes):
        if len(stack) == 0:
            stack.append((sidx, eidx))
            continue
        else:
            howWannOut = list(filter(lambda e: e[1] < sidx, stack))
            if howWannOut:
                ans += 1
                stack.clear()
                stack.append((sidx, eidx))
            else:
                stack.append((sidx, eidx))
    if stack:
        ans += 1
    return ans


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
