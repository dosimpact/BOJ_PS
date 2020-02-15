
# https://www.acmicpc.net/problem/2023
import sys


def input(): return sys.stdin.readline().rstrip()

# n까지의 소수 구하기a. 에라토스테네스의 체


N = int(input())
n = 1
for _ in range(N):
    n = n*10

# 소수의 갯수 , 소수가 담긴 배열, 체크 배열
pc = 0
#pn = [0]*(n+1)
check = [0]*(n+1)  # 0소수 1은 소수 아님 ( 2부터 가능 pc-1 까진)

for i in range(2, n+1):
    if check[i] == 0:
        #pn[pc] = i
        pc += 1
        for j in range(i*i, n+1, i):
            check[j] = 1
# for i in range(pc):
#     print(pn[i])
# d[i] i자리의 소수들(리스트) , -> d[i]는 d[i-1] + 한자리수 소수들 이 소수라면 append
d = [[] for i in range(N+1)]
dhanjari = [1, 3, 5, 7, 9]
for i in range(2, 10):
    if check[i] == 0:
        d[1].append(i)
for i in range(2, N+1):
    for e in d[i-1]:
        for han in dhanjari:
            now = int(str(e) + str(han))
            if check[now] == 0:
                d[i].append(now)
for e in d[N]:
    print(e)
