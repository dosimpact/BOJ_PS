

N, M, K = map(int, input().split())
arr = []
query = []
for _ in range(N):
    arr.append(int(input()))
for _ in range(M+K):
    query.append(list(map(int, input().split())))
tree = [0 for _ in range(len(arr)*4)]

# 1. basecase - return
# 2. propagation


def init(node: int, start: int, end: int):
    if start == end:  # basecase - leaf
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]


def update(node: int, start: int, end: int, idx: int, diff: int):
    # basecase - dont care
    if not(start <= idx and idx <= end):
        return
    tree[node] += diff
    # basecase - leaf node
    if start == end:
        return
    mid = (start+end)//2
    update(node*2, start, mid, idx, diff)
    update(node*2+1, mid+1, end, idx, diff)
    return


def segSum(node: int, start: int, end: int, L: int, R: int):
    # basecase - dont case
    if (end < L)or(R < start):
        return 0
    # basecase - under fetch
    if L <= start and end <= R:
        return tree[node]
    # over fetch
    mid = (start+end)//2
    return segSum(node*2, start, mid, L, R) + segSum(node*2+1, mid+1, end, L, R)


range_L, range_R = 0, len(arr)-1
init(1, range_L, range_R)
for q in query:
    a, b, c = q
    if a == 1:
        b -= 1
        diff = c - arr[b]  # 6 - 3
        arr[b] = c
        update(1, range_L, range_R, b, diff)
    if a == 2:
        print(segSum(1, range_L, range_R, b-1, c-1))
