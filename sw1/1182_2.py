
import sys


def input(): return sys.stdin.readline().rstrip()

"""
비트 마스크 연습
-전체 돌기
-부분 집합의 합 구해보기
"""
arr = [-7, -3, -2, 5, 8]
N = 5
S = 0

N, S = map(int, input().split())
arr = list(map(int, input().split()))

Counter = 0
for i in range(0, 1 << N, 1):
    #print(f"{i} > {bin(i)}")
    ans = 0
    for k in range(0, N, 1):
        if i & (1 << k):
            ans += arr[::-1][k]
    if ans == S:
        Counter += 1
    #print(f"ans : {ans}")
if S == 0:
    print(Counter-1)
else:
    print(Counter)
