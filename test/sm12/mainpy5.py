import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 두더지 게임
# N 정사, N제곱 마리 두더지
# 1초에 한번 두더지 친다. 두더지 점수 획득, 안치면 들어가
#


def main():
    # 데이터 파상, 1번 타임에 얻을 수 있는 점수들
    N = int(input())
    timer = dict()
    for _ in range(N**2):
        # 1 3 1 3 5 # 1번 두더지 점수, 3번올라온다, 1,3,5 타이밍에
        data = list(map(int, input().split()))
        score = data[0]
        cnt = data[1]
        ts = data[2:]
        for time in ts:
            if time in timer:
                timer[time].append(score)
            else:
                timer[time] = [score]
    ans = 0
    for key in timer.keys():
        ans += max(timer[key])
    print(ans)


if __name__ == "__main__":
    main()

"""
2
1 3 1 3 5
2 2 2 4
3 2 1 2
4 1 3
>13

1
1 4 1 6 9 4
>4

1
1 0
>0

1
100 1 99999999
>100
"""
"""
2
1 3 1 3 5 # 1번 두더지 점수, 3번올라온다, 1,3,5 타이밍에
2 2 2 4 # 2번 두다지 점순느 2점, 2번 올라온다, 2,4 타이밍에
3 2 1 2
4 1 3
"""
