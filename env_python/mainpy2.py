


# 세그먼트 트리
# 4배 메모리,루트1, node,start,end, 원본 업데이트 필요
# init,query,update

arr = []
tree = []


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

# 구간 합에 대한 요청


def query(node, start, end, L, R):
    # 요청이 과다,걸처있는 범위,상관없는 범위
    if R < start or end < L:
        return 0
    if L <= start and end <= R:
        return tree[node]
    mid = (start+end)//2
    res = query(node*2, start, mid, L, R) + query(node*2+1, mid+1, end, L, R)
    return res


def update(node, start, end, diff, idx):
    # 상관없는 범위 | 업데이트 | 전파 가능?
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start+end)//2
    update(node*2, start, mid, diff, idx)
    update(node*2+1, mid+1, end, diff, idx)


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0 for _ in range(len(arr)*4)]
init(1, 0, len(arr)-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, len(arr)-1, diff, b)
    else:
        # b,c 합 출력
        print(query(1, 0, len(arr)-1, b-1, c-1))

"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""
