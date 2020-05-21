import sys


def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

ansList = []


def hanoi(fr, by, to, n: int):
    global ansList
    if n == 1:
        ansList.append((fr, to))
        return
    hanoi(fr, to, by, n-1)
    ansList.append((fr, to))
    hanoi(by, fr, to, n-1)


N = int(input())
hanoi(1, 2, 3, N)
print(len(ansList))
for al in ansList:
    print(*al)
