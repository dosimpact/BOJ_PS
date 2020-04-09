
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


"""

"""

N = int(input())

ans = 0
for k in range(1, 10):
    a, b = 10**(k-1), 10**(k)
    if a <= N and N < b:
        ans += k*(N-a + 1)
        break
    ans += k*(b-a)

print(ans)
