

import sys


def input(): return sys.stdin.readline().rstrip()


Debug = False


"""

"""

su = list(input())
# 30의 배수가 되려면, 끝자리 숫자가 0이어야 되고, 모든 수의 합이 3의 배수이야 한다.

haszero = su.count('0')

if haszero <= 0:
    print(-1)
    exit(0)
allsusum = 0
for s in su:
    allsusum += int(s)

if allsusum % 3 != 0:
    print(-1)
    exit(0)
else:
    su.sort(reverse=True)
    print("".join(su))


"""
fb) 수의 특성을 파악하는 문제
1. 30의 배수 이려면 , 0 하나 이상 숫자에 포함되어야 하고
2. 30의 배수는 모든 각 자리수의 합이, 3의 배수이여야 한다.

1,2, 번 조건을 만족하면
내림차순 정렬을 통해 30의배수중 가장 큰것을 출력하면 된다.
"""
