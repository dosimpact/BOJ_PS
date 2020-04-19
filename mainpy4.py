

import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


N, L = map(int, input().split())

Lants = []
Rants = []

for i in range(1, N+1):
    ant = int(input())
    if ant < 0:
        Lants.append((abs(ant), i))
    else:
        Rants.append((ant, i))

Lants.sort(key=(lambda e: e[0]))
Rants.sort(key=(lambda e: e[0]))

print(Lants)
print(Rants)

ansT = max(Lants[-1][0], L-Rants[0][0])

ansI = None
if Lants[-1][0] < L-Rants[0][0]:
    ansI = Rants[0][1]
else:
    ansI = Lants[-1][1]
print(ansI, ansT)

"""

4 10
1
2
3
-4

4 10
2
3
-4
1

"""
