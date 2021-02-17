import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]

ans = 0
dPtn = len(data)-1
while K != 0 and dPtn >= 0:
    if data[dPtn] > K:
        dPtn -= 1
    if data[dPtn] <= K:
        K -= data[dPtn]
        ans += 1

print(ans)
