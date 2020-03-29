"""
결국 빨리 끝나는 것 중 빨리 시작하는 순서(시작과 끝이 같은 경우의 수를 걸러줌)대로 집어 넣으면,

더 빠르게 답을 구해낼 수 있다.
"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
inps = []
for _ in range(N):
    (a, b) = map(int, input().split())
    inps.append((a, b))

inps.sort(key=lambda x: (x[0]))
inps.sort(key=lambda x: (x[1]))


nowTime = 0
ans = 0
for inp in inps:
    if inp[0] >= nowTime:
        nowTime = inp[1]
        ans += 1
print(ans)
