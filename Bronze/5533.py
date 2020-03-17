"""

"""
import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = False
obj = {}

plen = int(input())
for i in range(plen):
    sel = list(map(int, input().split()))
    obj[i] = sel
    if DEBUG:
        print(obj)

ans = [0 for _ in range(plen)]  # 0번 ~ plen 까지
for rnd in range(3):
    cards = []
    for j in obj:
        cards.append(obj[j][rnd])
    for j in range(plen):
        if cards.count(cards[j]) == 1:
            ans[j] += cards[j]
for an in ans:
    print(an)
