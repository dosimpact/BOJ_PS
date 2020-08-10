import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


N = int(input())
A = [0] + list(map(int, input().split()))
d = [0 for _ in range(N + 1)]
dArray = [[] for _ in range(N + 1)]


d[1] = 1
dArray[1] = [A[1]]

for i in range(2, N + 1):
    d[i] = 1
    dArray[i] = [A[i]]

    # 이어붙일 인덱스를 선별한다.
    prevIdx = -1
    prevL = -1
    for j in range(1, i):
        if A[i] > A[j] and d[j] > prevL:
            prevL = d[j]
            prevIdx = j

    if prevIdx != -1:
        d[i] = prevL+1
        dArray[i] = dArray[prevIdx] + [A[i]]

# print(d)
# print(dArray)
resIdx = d.index(max(d))
print(d[resIdx])
print(*dArray[resIdx])

"""
10
10 20 30 40 1 2 3 4 5 6
"""
