
import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


N = int(input())
data = list(map(int, input().split()))

res = []

for i in range(1, len(data)+1):
    tmp = data[i-1]*i - sum(res[:i-1])
    res.append(tmp)
print(*res)
