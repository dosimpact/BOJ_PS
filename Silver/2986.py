import sys
DEBUG = False


def input(): return sys.stdin.readline().rstrip()


N = int(input())

anslist = []
for i in range(1, int(N**(1/2))+1, 1):
    if N % i == 0:
        anslist.append(i)
if DEBUG:
    print("-->1,", anslist)
anslist.pop(0)
if anslist:
    print(N - int(N/anslist[0]))
else:
    print(N-1)
