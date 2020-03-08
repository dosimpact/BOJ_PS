import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

# 해당 숫자의 2와 5의 소인수를 출력해주는 함수


def sol(n: int):  # 100 이라 가정
    e = 0
    i = 2
    while(i <= n):
        e += int(n/i)
        i = i*2
    o = 0
    i = 5
    while(i <= n):
        o += int(n/i)
        i = i*5
    return (e, o)


N, M = (map(int, input().split()))


two, five = sol(N)
btwo1, bfive1 = sol(M)
btwo2, bfive2 = sol(N-M)
res = (two - (btwo1+btwo2), five - (bfive1 + bfive2))
print(min(res))
