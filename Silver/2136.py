

import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


N, L = map(int, input().split())

Lants = []
Rants = []
ants = []

for i in range(1, N+1):
    ant = int(input())
    ants.append([(ant), i, None])
    if ant < 0:
        Lants.append((abs(ant), i))
    else:
        Rants.append((ant, i))

Lants.sort(key=(lambda e: e[0]))
Rants.sort(key=(lambda e: e[0]))
ants.sort(key=(lambda e: abs(e[0])))
for idx, ant in enumerate(ants):
    ant[2] = idx+1

# print(Lants)
# print(Rants)
# print(ants)

if len(Lants) == 0:
    print(ants[0][1], L-ants[0][0])
elif len(Rants) == 0:
    print(ants[-1][1], abs(ants[-1][0]))
else:
    ansT = max(Lants[-1][0], L-Rants[0][0])
    ansI = None
    if Lants[-1][0] < L-Rants[0][0]:
        index = len(Lants)+1
        ansI = list(filter(lambda e: e[2] == index, ants))[0][1]
    else:
        index = len(Lants)
        ansI = list(filter(lambda e: e[2] == index, ants))[0][1]
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

4 10
1
2
3
4

4 10
-1
-2
-3
-4

4 10
-4
-2
-3
-1
"""
