import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

a = 0
b = 0
su = 0
for i in range(1, 1001):
    b = a
    a += i
    if a >= N and N > b:
        su = i+1
        break
idx = N - (b+1)
top = su - (idx+1)
bot = idx+1
print(top, bot)
