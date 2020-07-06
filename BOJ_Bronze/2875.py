

import sys


def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())

team = min((n//2), (m//1))
last = (n+m) - (team*3)

#print(team, last)
if k <= last:
    print(team)
else:
    teambreak = k - last
    u, v = divmod(teambreak, 3)
    if v != 0:
        u += 1
    print(team - u)
