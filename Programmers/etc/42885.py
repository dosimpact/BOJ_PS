
import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()


def solution(ps: [], lmt: int):
    ps = sorted(ps)
    ans = 0
    check = [0 for _ in range(len(ps))]
    min_idx = 0
    max_idx = len(ps) - 1
    while(min_idx < max_idx):
        if ps[min_idx] + ps[max_idx] <= lmt:  # 축하 ! - > min 증가 max증가 ans 하나 증가 체크
            check[min_idx] = check[max_idx] = 1
            ans += 1
            min_idx += 1
            max_idx -= 1
        else:
            max_idx -= 1
    for c in check:
        if c == 0:
            ans += 1
    return ans


"""
FB) 복기
1. 시간 복잡도 생각 N = 5만
 -> 무조건 N 이 나와야 하는 상황

2. FB) 정렬후 , 최소값 + 범위내 적당히 큰 최댓값 <= 리미트 
-> 이것이 내부 원소들도 쌍을 이룰거라는 생각
"""
