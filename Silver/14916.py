
import sys


def input(): return sys.stdin.readline().rstrip()

"""
동전의 갯수 최소,
"""

n = int(input())

ans = 0


for i in range(n//5, -1, -1):  # 13 > 2 1 0
    ansTmp = i
    nTmp = n - (5*i)
    if nTmp % 2 == 0:
        ansTmp += nTmp // 2
        print(ansTmp)
        exit(0)
    else:
        pass

print(-1)
