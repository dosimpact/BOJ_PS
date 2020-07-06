

import sys


def input(): return sys.stdin.readline().rstrip()


r, c = map(int, input().split())

card = [["." for _ in range(c*2)] for _ in range(r*2)]

for i in range(r):
    ins = list(input())
    for j in range(len(ins)):
        card[i][j] = ins[j]

# 대칭 1

for i in range(r):
    for j in range(c):
        card[i][(2*c-1) - j] = card[i][j]


# 대칭 2
for i in range(r):
    for j in range(c*2):
        card[(2*r-1) - i][j] = card[i][j]


a, b = map(int, input().split())

if card[a-1][b-1] == '#':
    card[a-1][b-1] = '.'
else:
    card[a-1][b-1] = '#'

for crd in card:
    for cr in crd:
        print(cr, end="")
    print()


"""
3 2
#.
.#
#.
3 3

4 2
#.
.#
#.
..
3 3

1 1
.
1 1

1 1
#
2 2

10 10
.........#
.........#
.........#
.........#
.........#
.........#
.........#
.........#
.........#
.#######.#
1 1

1 2
#.
1 1

1 2
#.
2 2
"""
