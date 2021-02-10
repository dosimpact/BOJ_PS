import sys

sys.setrecursionlimit(10**6)

memo = [0 for _ in range(101)]


def fibo(n: int):
    if memo[n]:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n-1)+fibo(n-2)
    return memo[n]


print(fibo(0))
print(fibo(10))
print(fibo(50))
