from sys import stdin
input = stdin.readline


tree = None
data = None
ans_max = -1
# back propagation


def init(node, start, end):
    global ans_max

    if start == end:
        tree[node] = (data[start], data[end])
        ans_max = max(ans_max, data[start])
        return tree[node]
    mid = (start+end)//2
    A = init(node*2, start, mid)
    B = init(node*2+1, mid+1, end)
    tree[node] = (min(A[0], B[0]), min(A[1], B[1]))

    ans_max = max(ans_max, (end-start+1)*tree[node][0])
    return tree[node]


while True:
    ans_max = -1
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    data = data[1:]
    tree = [(0, 0) for _ in range(len(data)*4)]
    init(1, 0, len(data)-1)
    print(ans_max)


"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0

4 1 2 3 4
0
>6

4 1 2 0 4
0
"""
