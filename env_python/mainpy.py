
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ans = min(N // 5, (N+M) // 12)
    print(ans)
