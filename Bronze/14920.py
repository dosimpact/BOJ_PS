import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

d = [0 for _ in range(100001)]

d[1] = N

for i in range(1, 100000):
    # 현재 수열이 1인지 아닌지 판단하기 | 아직 1 이 아니라면 다음 수열 구하기
    if d[i] == 1:
        print(i)
        break
    # print(d[i])
    if (d[i]) % 2 == 0:
        d[i+1] = d[i]//2
    else:
        d[i+1] = d[i]*3+1
