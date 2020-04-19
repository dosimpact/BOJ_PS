

import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


def check(su: int):
    su = str(su)
    if su.count('6') >= 3:
        while su.count('6') >= 3:  # 3이상이면 계속 시도
            su = su[su.index('6'):]
            if su[:3] == '6'*3:
                return True
            else:
                su = su[1:]
        return False
    else:
        return False


N = int(input())

su = 666
Nth = 1  # 현재 Nth번째 제목
while Nth < N:
    su += 1
    if check(su):  # 조건에 맞으면 해당수를 임명
        Nth += 1
        # print(f"{su},{Nth}")
print(su)
