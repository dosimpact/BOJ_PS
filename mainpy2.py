"""
순열릐 순서

1~N 까지 

"""

import sys
from math import factorial
from itertools import permutations


def input(): return sys.stdin.readline().rstrip()


def solve1(n: int, k: int):
    # N은 4이고, K 는 3
    elist = [i for i in range(1, n+1)]  # 1 2 3 4
    ans = []
    for i in range(n):  # 0번쨰부터 채워나갈래
        cnt = 0
        a = 0
        b = factorial(n - (i+1))
        while(True):
            if a <= k and k < b:
                break
            else:
                cnt += 1
                a = b
                b += factorial(n - (i+1))
        k = k - a
        ans.append(elist[cnt])
        elist.pop(cnt)
    print(ans)


def solve2(t: []):
    pass


N = int(input())
num, *b = map(int, input().split())

if num == 1:
    solve1(N, b[0])
else:
    solve2(b)
