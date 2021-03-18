import sys


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N, M, K = map(int, input().split())  # 숫자 갯수, 업데이트 수 , 구간합 요청 수
arr = [int(input()) for _ in range(N)]
query = []
for _ in range(M + K):
    a, b, c = map(int, input().split())
    query.append((a, b, c))

tree = [0 for _ in range(len(arr) * 4)]


def seg_init(node: int, start: int, end: int):
    # 리프 노드면 대입, 아니라면 전파
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = seg_init(node * 2, start, mid) + seg_init(node * 2 + 1, mid + 1, end)
    return tree[node]


def seg_sum(node: int, start: int, end: int, L: int, R: int):
    # 구간에 상관없으면 0 , 요청이 과다하면 전부 , 그외 전파
    if R < start or end < L:
        return 0
    if L <= start and end <= R:
        return tree[node]
    mid = (start + end) // 2
    return seg_sum(node * 2, start, mid, L, R) + seg_sum(
        node * 2 + 1, mid + 1, end, L, R
    )


def seg_update(node: int, start: int, end: int, idx: int, diff: int):
    # 업데이트 구간 상관없으면 리턴, 업뎃 후 , 리프가 아니라면 전파
    if not (start <= idx and idx <= end):
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    seg_update(node * 2, start, mid, idx, diff)
    seg_update(node * 2 + 1, mid + 1, end, idx, diff)


seg_init(1, 0, len(arr) - 1)
for a, b, c in query:
    if a == 1:  # b를 c로 바꾼다.
        b = b - 1
        diff = c - arr[b]
        arr[b] = c
        seg_update(1, 0, len(arr) - 1, b, diff)
    else:  # b~c 구간합을 구한다.
        print(seg_sum(1, 0, len(arr) - 1, b - 1, c - 1))

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
