
import sys


def input(): return sys.stdin.readline().rstrip()


LIMIT_N = 100001
N, K = map(int, input().split())

fromidx = [-1 for _ in range(LIMIT_N)]
check = [-1 for _ in range(LIMIT_N)]
check[N] = 0
q = [N]


def inRange(x):
    return x >= 0 and x < LIMIT_N


while q:
    now = q.pop(0)
    if now == K:
        break
    for nxt in [now*2, now+1, now-1]:
        if not inRange(nxt) or check[nxt] != -1:
            continue
        check[nxt] = check[now] + 1
        fromidx[nxt] = now  # 야 nxt(10)노드 너는 누구로부터 왔니?
        q.append(nxt)
print(check[K])

p = K
trace = []
while True:
    # print(p, end=" ")
    trace.append(p)
    if p == N:
        break
    p = fromidx[p]
    # print(trace)
print(*trace[::-1])
"""
5 17


5 -> 10
"""
