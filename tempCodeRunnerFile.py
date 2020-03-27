import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = True

N = int(input())
inps = list(map(int, input().split()))

ans_max = []
for i in range(100000, -1, -1):  # i개의 말이 참일때
    if inps.count(i) == i:
        print(i)
        exit(0)
print(-1)

# if ans_max[0] == 0:
#     print(-1)
# else:
#     print(ans_max[0])
# 가정을 하는거야, i개의 말이 참일때, i개의 말이 참이라는 명제를 말한것들의 갯수를 구해 -> 그게 i랑 동일하면 넣어.
