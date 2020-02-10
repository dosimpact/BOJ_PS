import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
data = [i for i in range(1, n+1)]
ans = []
i = 0
for _ in range(n):
    # 현재위치에서 k-1만큼 이동후 len나눠
    i = (i + k - 1) % len(data)
    ans.append(data.pop(i))

print('<', end='')
for i, e in enumerate(ans):
    if i == len(ans) - 1:
        print(e, end='')
    else:
        print(e, end=', ')
print('>', end='')
