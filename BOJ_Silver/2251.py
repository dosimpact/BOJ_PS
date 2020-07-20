import sys

input = sys.stdin.readline

X, Y, Z = map(int, input().split())

total_water = Z
init_state = (0, 0, Z)
check = [[-1 for _ in range(201)] for _ in range(201)]

res = [Z]  # A가 비어있을때, C의 양을 구하시오
# 시작
q = [(0, 0)]  # A B 의 물의 양이 q에 들어간다.
check[0][0] = 1


def makeNext(a: int, b: int, c: int):
    res = []
    # A -> B
    na, nb, nc = 0, a+b, c
    if nb > Y:
        na, nb, nc = a+b - Y, Y, c
    res += [(na, nb, nc)]
    # A -> C
    na, nb, nc = 0, b, a+c
    if nc > Z:
        na, nb, nc = a+c - Z, b, Z
    res += [(na, nb, nc)]
    # B -> A
    na, nb, nc = a+b, 0, c
    if na > X:
        na, nb, nc = X, a+b-X, c
    res += [(na, nb, nc)]
    # B -> C
    na, nb, nc = a, 0, b+c
    if nc > Z:
        na, nb, nc = a, b+c-Z, Z
    res += [(na, nb, nc)]
    # C -> A
    na, nb, nc = a+c, b, 0
    if na > X:
        na, nb, nc = X, b, a+c-X
    res += [(na, nb, nc)]
    # C -> B
    na, nb, nc = a, b+c, 0
    if nb > Y:
        na, nb, nc = a, Y, b+c-Y
    res += [(na, nb, nc)]
    return res


while q:
    a, b = q.pop(0)
    c = total_water - (a+b)
    for na, nb, nc in makeNext(a, b, c):
        if check[na][nb] == -1:
            check[na][nb] = 1
            q += [(na, nb)]
            if na == 0:
                res += [nc]

res = set(res)
res = list(res)
res.sort()
print(*res)
"""
8 9 10 = X,Y,Z

0 0 10
0 0 10 ( 0, a+b, c)
a + b > 9

( a+b - 9 , X , c)


1 200 200

0 0 200 *
1 0 199
0 1 199 *
1 1 198
0 2 198 *

"""
