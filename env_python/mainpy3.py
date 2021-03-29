from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)

# 예산 분배, 이분탐색
# 조건 - 예산 상한액 다 만족 ?
# 그러면서 - 최대 예산 분배


N = int(input())
data = list(map(int, input().split()))
M = int(input())

# left, right = 0, M
left, right = 0, max(data)  # !범위 1부터아님


def check(unit: int):
    total = M
    for d in data:
        if unit < d:
            total -= unit
        else:
            total -= d
    return total >= 0


ans_max = left  # 최적해
while left <= right:
    mid = (left + right) // 2
    if check(mid):  # 조건 -  좌향 조정
        ans_max = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans_max)


"""
3
10 10 10
1
>1 ❌  예산의 범위 0 도 가능!
>0

❌ - 예산액이 충분한 경우
3
10 9 8
100
>100❌
>10
"""