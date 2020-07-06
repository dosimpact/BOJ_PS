
import sys

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


bd = []

for _ in range(5):
    l = input()
    bd.append(l)

maxlen = 0
for b in bd:
    maxlen = max(len(b), maxlen)

if DEBUG:
    print(maxlen)
    print(bd)

for i in range(len(bd)):
    bd[i] = bd[i].ljust(maxlen, ' ')

if DEBUG:
    print(maxlen)
    print(bd)

for i in range(len(bd[0])):
    for j in range(len(bd)):
        if bd[j][i] != ' ':
            print(bd[j][i], end="")
