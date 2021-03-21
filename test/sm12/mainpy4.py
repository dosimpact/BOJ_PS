import sys
import heapq
import re
import math
from collections import deque
from typing import *
from math import ceil

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 발판 밝기 (ep 필요)
# N개의 발판 양의 정수 , 음의 정수
# 밟으면 그 숫자만큼 이동
# 1,2,3 에서 시작 가능
# 또 밝으면 종료
# 최대 밟는 수
# out of range 고려 X


def main():
    N = int(input())
    steps = list(map(int, input().split()))
    ans = []
    for i in range(3):  # 0,1,2
        check = [False for _ in range(N)]
        # check[i] = True
        q = [i]
        while q:
            now = q.pop(0)
            if check[now]:
                break
            nxt = now + steps[now]
            check[now] = True
            q.append(nxt)
        # print(check)
        ans.append(check.count(True)+1)
    print(max(ans))


if __name__ == "__main__":
    main()

"""
10
3 5 -1 -2 4 4 3 -2 -3 -2
>8

3
1 -1 -1
>4
"""
