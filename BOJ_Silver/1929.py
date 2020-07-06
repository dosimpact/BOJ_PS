
import sys


def input(): return sys.stdin.readline().rstrip()

# n까지의 소수 구하기a. 에라토스테네스의 체


m, n = map(int, input().split())

# 소수의 갯수 , 소수가 담긴 배열, 체크 배열
pc = 0
pn = [0]*(n+1)
check = [0]*(n+1)

for i in range(2, n+1):
    if check[i] == 0:
        check[i] = 1
        pn[pc] = i
        pc += 1
        for j in range(i*i, n+1, i):
            check[j] = 1
for i in range(pc):
    if pn[i] >= m:
        print(pn[i])
