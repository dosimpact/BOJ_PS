from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline


def ParseSec(s: str):
    res = 0
    for unit in s.split(":"):
        res = res * 60
        res += int(unit)
    return res


N, total = input().split()
N = int(N)
total_time = ParseSec(total)
arr = []
for _ in range(N):
    arr.append(ParseSec(input().strip()))
print(total_time, arr)

ans = (0, 0)
left, right = 0, 0
# 연습시간이 부족 > 우향 조정, 초과 > 좌향조정
# 우향 조정끝이면 종료
while right < len(arr):
    tmp = sum(arr[left : right + 1])  # 0 1
    if tmp >= total_time:
        if ans[0] < (right - left + 1):
            ans = (right - left + 1, left + 1)
        left += 1
    else:
        right += 1
print(*ans)

"""
7 00:05:48
02:14
03:34
02:34
03:45
05:43
01:34
02:33
"""