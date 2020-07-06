import sys


def input(): return sys.stdin.readline().rstrip()


N, L = map(int, input().split())

# for i in range(L, 100): # fb 100보다 크거나 = 길이 100까진 괜찮아......
for i in range(L, 101):
    # 현재 길이가 i 인것부터 만들어 볼래

    sb = 0
    for j in range(1, i):
        sb += j
    d, m = divmod(N-sb, i)
    #print("-->", i, sb, d, m)
    # if m == 0: (-30)//10 은 -3
    if m == 0 and d >= 0:  # fb)(N-S) // i 한 결과가 음이 될수도
        ans = ([k for k in range(d, d+i)])
        for an in ans:
            print(an, end=" ")
        sys.exit(0)
print(-1)
