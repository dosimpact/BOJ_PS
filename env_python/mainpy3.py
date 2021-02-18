import sys
import math
from typing import *

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def solution(ans: List[int]):
    p1, p2, p3 = 0, 0, 0
    p1n = [1, 2, 3, 4, 5]  # 0,1,2,3,4 | 0,1,2,3,4
    p2n = [2, 1, 2, 3, 2, 4, 2, 5]
    p3n = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(ans)):
        # print(p1n[i % len(p1n)])
        p1 += 1 if p1n[i % len(p1n)] == ans[i] else 0
        p2 += 1 if p2n[i % len(p2n)] == ans[i] else 0
        p3 += 1 if p3n[i % len(p3n)] == ans[i] else 0
    pns = [p1, p2, p3]
    winnerCnt = max(pns)
    result = []
    for i in range(3):
        if winnerCnt == pns[i]:
            result += [i + 1]
    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
