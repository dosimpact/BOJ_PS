
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


saram = int(input())
gamesu = int(input())
target = list(map(int, input().split()))  # 1 2 3 2

res = [0 for _ in range(saram)]  # 0 0 0

for nth in range(gamesu):
    submit = list(map(int, input().split()))  # 1 1 2
    t = target[nth]  # 1 > 2 > 3 > 2
    X = saram
    for i in range(len(submit)):
        if t == submit[i]:
            res[i] += 1
            X -= 1
    res[t-1] += X

for re in res:
    print(re)
