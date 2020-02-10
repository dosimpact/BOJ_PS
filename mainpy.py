import sys


def input(): return sys.stdin.readline().rstrip()


data = []
N = int(input())

for _ in range(N):
    a, *b = input().split()
    if a == 'push':
        data.append(b[0])
    if a == 'pop':
        print(data.pop() if len(data) > 0 else -1)
    if a == 'size':
        print(len(data))
    if a == 'empty':
        print(1 if len(data) == 0 else 0)
    if a == 'top':
        print(data[-1] if len(data) > 0 else -1)
