

import sys
from copy import deepcopy
from collections import defaultdict
import math

sys.setrecursionlimit(10**8)

"""

"""


def solution(n, k):  # 3 , 5
    answer = []
    k -= 1
    data = [i for i in range(1, n+1)]

    while k != 0:  # n은 현재 남은 자리수, k번째
        u, v = divmod(k, math.factorial(n-1))  # 2, 0 <
        answer.append(data.pop(u))
        k = v
        n -= 1
    answer.extend(data)

    return answer


print(solution(3, 5))
