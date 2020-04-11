import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()

"""
부등호 문제
k개 부등호 > k+1 개 정수 가능
a
k : [2,9] k가 9라면 10개의 정수 0 ~ 9 까지지.

최대를 만들려면 > `` K+1 개 9부터 고른다.
최소를 만들려면 > k+1개 0부터 고르고

백트래킹 + 재귀로

"""
K = int(input())
BList = list(input().split())
L = K+1


def isPoss(a: int, e: str, b: int):
    #print(f"{a} {e} {b}")
    if e == '<':
        return a < b
    elif e == '>':
        return a > b
    else:
        return "ERROR"


def go(idx: int):  # 현재 고를 인덱스,

    # 다고른경우 | 최종 점검후에 부등호를 만족한다면 정답출력
    if idx == L:
        res = [data[i] for i in IAns]
        # print((res))
        Ans.append(res)
        return

    for i in range(0, K+1):  # 0번부터 k번 인덱스까지
        if Check[i]:
            continue
        #print(f"{isPoss(data[idx-1], BList[idx-1], data[idx])}")
        if idx != 0 and not isPoss(data[IAns[idx-1]], BList[idx-1], data[i]):
            continue
        Check[i], IAns[idx] = True, i
        go(idx+1)
        Check[i] = False


Ans = []
IAns = [0]*(L)  # 인덱스를 담는 배열 012,021...
Check = [0]*(L)  # 해당 인덱스가 사용중인지..
data = [i for i in range(9, -1, -1)][:L]  # 최소 데이터로
go(0)
IAns = [0]*(K+1)  # 인덱스를 담는 배열 012,021...
Check = [0]*(K+1)  # 해당 인덱스가 사용중인지..
data = [i for i in range(0, 10, 1)][:K+1]  # 최소 데이터로
go(0)


Ans.sort(reverse=True)
print(*Ans[0])
print(*Ans[-1])
