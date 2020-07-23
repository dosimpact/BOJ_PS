import sys


input = sys.stdin.readline

N, K = map(int, input().split())


LIMIT_N = 100001

check = [-1 for _ in range(LIMIT_N)]
cnt = [-1 for _ in range(LIMIT_N)]

check[N] = 0
cnt[N] = 1
q = [N]
# BFS 알고리즘을 통해, x -> x-1,x+1,x*2 을 탐색한다.


def inRange(x):
    return x >= 0 and x < LIMIT_N


while q:
    now = q.pop(0)
    for next in [now-1, now+1, now*2]:
        if not inRange(next):
            continue
        if check[next] == -1:
            check[next] = check[now] + 1
            cnt[next] = cnt[now]
            q.append(next)
        else:
            if check[next] == check[now] + 1:
                cnt[next] += cnt[now]

print(check[K])
print(cnt[K])
