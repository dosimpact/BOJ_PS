import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 이용자 인원수 ,소까존 도착 시간 입력
# 모든 인원이 쏘카존에 올 수 있는 시간 구간 > 스 시간에 빌릴 수 있는 차 추천

N = int(input())
left, right = 0, 0


def parseInput():
    l, r = input().split("~")
    lm, ls = map(int, l.split(":"))
    rm, rs = map(int, r.split(":"))
    l, r = lm*60 + ls, rm*60+rs
    return (l, r)


def parseOutput(l, r):
    lm, ls = map(str, (l // 60, l % 60))
    rm, rs = map(str, (r // 60, r % 60))
    l = f"{lm.rjust(2,'0')}:{ls.rjust(2,'0')}"
    r = f"{rm.rjust(2,'0')}:{rs.rjust(2,'0')}"
    res = f"{l} ~ {r}"
    return res


ans_l, ans_r = None, None
for _ in range(N):
    l, r = parseInput()

    # 초기 경우
    if ans_l == None and ans_r == None:
        ans_l, ans_r = l, r
        continue
    # 정답이 될 수 없는경우
    if r < ans_l or ans_r < l:
        print(-1)
        exit(0)
    # 범위가 줄어드는 경우
    if ans_l < l:
        ans_l = l
    if r < ans_r:
        ans_r = r
print(parseOutput(ans_l, ans_r))

"""
3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00
>14:00 ~ 18:00

3
12:00 ~ 23:59
11:00 ~ 18:00
01:00 ~ 02:00
>-1

3
12:00 ~ 23:59
12:00 ~ 12:00
12:00 ~ 12:00
>12:00 ~ 12:00
"""
