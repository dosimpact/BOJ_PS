import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


def draw(N: int, cnt: int):
    if cnt == 1:
        print(" " * (N - 1) + "*")
        return
    else:
        print(" " * (N - cnt) + "*" + " " * (((cnt - 1) * 2) - 1) + "*")


for i in range(1, N + 1):
    draw(N, i)
