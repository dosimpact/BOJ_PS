
import sys


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

# 남은 설탕 | 5


def go(sugar, o, sam):
    global slist
    if sugar == 0:
        slist.append(o+sam)
        return
    else:
        if sugar >= 5:
            go(sugar-5, o+1, sam)
        if sugar >= 3:
            go(sugar-3, o, sam+1)
        return -1


slist = []
s = int(input())
go(s, 0, 0)
print(-1 if len(slist) == 0 else min(slist))
