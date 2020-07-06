
import sys
import math
import functools
import itertools

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


score = []

for i in range(1, 9):
    now = int(input())
    score.append([now, i])

score.sort(key=lambda x: (-x[0]))

final = score[0:5]

final_sum = 0
for e in final:
    final_sum += e[0]
print(final_sum)
final.sort(key=lambda x: (x[1]))
for e in final:
    print(e[1], end=' ')
