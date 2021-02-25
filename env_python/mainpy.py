import sys
import math
from typing import *


# 나누어 떨어지면,  몫 -1, 나머지 3 유지
def solution(n):
    ans=""
    while n >0:
        a,b = divmod(n,3)
        if b == 0:
            a -=1
            b = 4
        ans += str(b)
        n = a

    return ans[::-1]

for i in range(1,15):
    print(solution(i))