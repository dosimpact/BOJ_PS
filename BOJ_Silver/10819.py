import sys
from itertools import permutations


def input(): return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
pit = list(permutations(arr))


def sol(arr):
    ans = 0
    for i in range(len(arr)-1):  # 6
        ans += abs(arr[i] - arr[i+1])
    return ans


maxans = 0
for it in pit:
    maxans = max(maxans, sol(it))

print(maxans)
