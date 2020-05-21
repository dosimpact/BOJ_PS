import sys


def input(): return sys.stdin.readline().rstrip()


x, y, w, h = map(int, input().split())

anslist = []

anslist.append(abs(0-x))
anslist.append(abs(w-x))
anslist.append(abs(0-y))
anslist.append(abs(h-y))

print(min(anslist))
