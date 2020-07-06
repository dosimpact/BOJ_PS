import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = True

while True:
    cnt = 0
    inps = list(map(int, input().split()))
    if inps[0] == -1:
        exit(0)
    for ins in inps[:-1]:
        if inps.count(ins*2) >= 1:
            cnt += 1
    print(cnt)
