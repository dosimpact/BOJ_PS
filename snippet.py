import sys


def input(): return sys.stdin.readline().rstrip()


an, am = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(an)]

bn, bm = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(bn)]

#print(A, B)

C = [[0 for j in range(bm)] for i in range(an)]

for i in range(an):
    for j in range(bm):
        res, it = 0, am
        for k in range(it):
            res += A[i][k]*B[k][j]
        C[i][j] = res

for e in C:
    print(*e)
