"""
각 카드에는 양의 정수

N장의 카드 중에서 3장의 카드를 골라야 한다.
고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
"""
# https://www.acmicpc.net/problem/2798
import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

# 고른수의 합, 몇개 고른겨? 현재 골르 인덱스


def go(susum: int, count: int, idx: int):
    global Ans
    # count가 3이면 체크후 중단
    if count >= 3:
        if susum <= m:
            Ans = max([Ans, susum])
        return
    if idx >= len(cards):
        return
    go(susum, count, idx+1)
    go(susum+cards[idx], count+1, idx+1)


Ans = -1
n, m = map(int, input().split())
cards = list(map(int, input().split()))
# print(cards)
go(0, 0, 0)
print(Ans)
