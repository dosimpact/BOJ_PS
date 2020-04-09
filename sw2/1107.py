
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


"""
무적권 : 번호를 누루고 > +,- 이동한다.
현재 채널은 100번
이동하려는 채널은 0 ~ 500,000 > 임의로, [0,1000,000) 움직이면서 최소값 해보자.
"""

N = int(input())  # 원하는 채널
M = int(input())  # 고장난 버튼의수
BList = set()
if M != 0:
    BList = set(map(int, input().split()))  # 이거는 못누름


Ans = abs(100-N)


def canI(i):
    if i == 0:
        # if 0 in BList:
        #     return True
        if 0 in BList:
            return False
        else:
            return True
    while i > 0:
        a = i % 10
        if a in BList:
            return False
        i = i // 10
    return True


for i in range(0, 10**6):
    if canI(i):
        Ans = min(Ans, len(str(i)) + abs(i-N))
print(Ans)
"""
fb) 숫자의 각 자리수 구하는 로직에서 주의할점 : 0 뺴고 다 된다.

fb) 입력에서 주의할점 : 고장난 버튼이 없는경우 : 3번째 입력이 주어지지 않는다.

fb) BreakList에서 있는지 없는지 여부를 반대로 했다.
-set으로 혹은 check배열로 해도 된다.
"""

"""
100
10
0 1 2 3 4 5 6 7 8 

0
--
101
10
0 1 2 3 4 5 6 7 8 

0

"""
