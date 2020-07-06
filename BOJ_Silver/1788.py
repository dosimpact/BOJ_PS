"""

피보나치 단순 공식의 확장

"""

import sys
import time

DEBUG = False
start = time.time()

memo = {}


def input(): return sys.stdin.readline().rstrip()


diver = 10**9
SIZE = 10**6

memo[-1] = 1
memo[0] = 0
memo[1] = 1

for i in range(1, SIZE+1):  # 1 0 -1
    memo[i] = (memo[i-1]+memo[i-2]) % diver


n = int(input())

if n >= 0:
    print(1) if n != 0 else print(0)
    print(memo[n])
else:
    n = abs(n)
    if n % 2 == 0:
        print(-1)
        print(memo[n])
    else:
        print(1)
        print(memo[n])

if DEBUG:
    print("time(s): ", time.time() - start)
# print(memo[2])
# print(memo[3])
# print(memo[4])
# print(memo[5])
# print(memo[6])
# print(memo[7])
# print(memo[SIZE])

# print(memo[-2])
# print(memo[-3])
# print(memo[-4])
# print(memo[-5])
# print(memo[-6])
# print(memo[-7])
# print(memo[-SIZE])

# 짝수이면 -> -만 붙이면 된다.
