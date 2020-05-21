import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
p = list(map(int, input().split()))
p.sort()
res = [0]*(len(p))
res[0] = p[0]
for i in range(1, len(res)):
    res[i] = res[i-1]+p[i]
print(sum(res))
