import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

ans = "YES" if (N % 3 == 0) or (M % 3 == 0) else "NO"
print(ans)
