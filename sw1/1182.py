

import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
Debug = True


def dprint(s: str):
    if Debug:
        print(f' DEBUG : {s} ')


def input(): return sys.stdin.readline().rstrip()


"""
https://www.acmicpc.net/problem/6603


- 가지치기가 안되는 BF 이다.
부분집합이므로, S가 완성이 되어도, 계속 부분집합을 만들다 보면, S가 안되는 경우가있다.
그래서 이 경우는 다 해봐야 한다.



- 예외처리

공집합인 경우도 있다.
S가 0이 아닐때면 알아서 걸러지는데
0인 경우라면 공집합도 하나를 잡아먹는다.
그러기때문에, S=0인경우에는 특별하게 공집합을 제거해준다.
"""


def go(idx: int, acc: int):

    # 인덱스가 끝으로 도달한 경우
    if idx >= len(datas):
        if acc == S:
            return 1
        return 0
    # 안되는 경우는 없음

    # keep
    res = 0
    res += go(idx+1, acc+datas[idx])
    res += go(idx+1, acc)
    return res


N, S = map(int, input().split())
datas = list(map(int, input().split()))
if S == 0:
    print(go(0, 0)-1)
else:
    print(go(0, 0))
