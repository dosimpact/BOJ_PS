"""
# 자주쓰는 알고리즘

-트라이 자료구조 구현하기✅
-행렬 회전하기 시계방향 90됴 ( 노말버전, 파이썬 버전 )✅
-다음 순열 구현하기 ✅
-비트마스크로 모든 집합 순회하기 (1182 BOJ) ✅

"""

import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


N = int(input())
data = list(map(int, input().split()))

res = []

for i in range(1, len(data)+1):
    tmp = data[i-1]*i - sum(res[:i-1])
    res.append(tmp)
print(*res)
