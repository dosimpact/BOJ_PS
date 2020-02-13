
import sys


def input(): return sys.stdin.readline().rstrip()


SIZE = 1001


n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(n)]

# d[][] i,j, 까지 갔을때 주은 최대 사탕 갯수
# d[][] = max (d[-1][] d[][-1] d[-1][-1] ) + data[][]

d = [[-1 for _ in range(m)] for _ in range(n)]


def dp(i, j):
    if (i, j) == (0, 0):
        return data[0][0]
    if d[i][j] != -1:
        return d[i][j]
    else:
        d[i][j] = data[i][j]
        maxval = []
        if i - 1 >= 0:
            maxval.append(dp(i-1, j))
        if j - 1 >= 0:
            maxval.append(dp(i, j-1))
        if i - 1 >= 0 and j - 1 >= 0:
            maxval.append(dp(i-1, j-1))
        d[i][j] += max(maxval)
        return d[i][j]


dp(n-1, m-1)
print(d[n-1][m-1])
