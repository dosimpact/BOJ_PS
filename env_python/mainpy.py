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
        # K 가 4000 이고 1000원으로 깎을 수 있다면
        d, m = divmod(K, data[dPtn])
        K = m
        ans += d

print(ans)
