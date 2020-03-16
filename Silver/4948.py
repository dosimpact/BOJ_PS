import sys
DEBUG = True


def input(): return sys.stdin.readline().rstrip()


"""
n보다 크고, 2n보다 작거나 같은 소수
적어도 하나 존재
"""

# 에라토스 체
SIZE = 123456
check = [0 for _ in range(SIZE*2 + 1)]

for i in range(2, SIZE*2+1):
    if check[i] == 0:
        for j in range(i*2, SIZE*2+1, i):
            check[j] = 1

while True:
    n = int(input())
    if n == 0:
        exit(0)
    ans = 0
    for i in range(n+1, n*2+1):
        if check[i] == 0:
            ans += 1
    print(ans)
