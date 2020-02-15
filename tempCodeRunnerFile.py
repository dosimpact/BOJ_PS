
import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())

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
