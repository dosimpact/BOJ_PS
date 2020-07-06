
import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())

# N에서 계속  9*1  90*2를 뺼 수 있을떄까지 뺀다. -> k범위 확인
krange = 0
jari = 1
now = 9
while(True):  # now를 9 90 900 씩 키우면서, n를 최대한 뺀다.
    if n > now:
        n = n - now
        krange += now*jari
        jari += 1
        now = int(str(now)+'0')
    else:
        krange += n*jari
        break
if krange < k:
    print(-1)
    sys.exit()

# k를 계속해서 9*1  90*2를 뺼 수 있을떄까지 뺀다.
jari = 1
while(True):
    dk = 9
    for _ in range(1, jari):
        dk = dk*10
    dk = dk * jari
    if k > dk:
        k = k - dk
        jari += 1
    else:
        break

k -= 1
(nth, nthjari) = divmod(k, jari)
ans = 1
for _ in range(1, jari):
    ans = ans*10
ans += nth
ans = str(ans)[nthjari]
print(ans)
