from sys import stdin
input = stdin.readline


tree = None
data = None
ans_max = -1
# back propagation


def init(node, start, end):
    if start == end:
        tree[node] = (data[start], start)
        return tree[node]
    mid = (start+end)//2
    A = init(node*2, start, mid)  # (최소높이,그 인덱스)
    B = init(node*2+1, mid+1, end)

    if A[0] > B[0]:
        tree[node] = B
    else:
        tree[node] = A
    return tree[node]


def query(node, start, end, L, R):
    # 요청이랑 상관없다. |
    w = (end-start+1)
    h, h_idx = tree[node]  # 최소 높이와 그 인덱스

    A = query(node*2, start, h_idx)
    B = query(node*2+1, start)

    return


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

4 4 4 4 1
0
>12 ❌
"""
