import sys
import math
from typing import *

sys.setrecursionlimit(10 ** 6)


input = sys.stdin.readline


def solution(array: List[int], commands: List[List[int]]):
    ans: List[int] = []
    for i, j, k in commands:
        nArr = array[i - 1 : j]
        nArr.sort()
        ans += [nArr[k - 1]]
    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
