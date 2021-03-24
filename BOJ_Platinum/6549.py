import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 트리노드에는 (최소값,인덱스) 를 넣는다.
# 세그먼트노드 = 현재 구간에서의 ( 최소값,그 인덱스)
tree = None
arr = None
# 리프노드 - backpropa
def init(node, start, end):
    global tree
    if start == end:
        tree[node] = (arr[start], start)
        return tree[node]
    mid = (start + end) // 2
    ltree = init(node * 2, start, mid)
    rtree = init(node * 2 + 1, mid + 1, end)

    if rtree[0] < ltree[0]:
        tree[node] = rtree
    else:
        tree[node] = ltree
    return tree[node]


# 해당 구간에서의 최소값,인덱스
def query(node, start, end, L, R):
    # 범위가 밖인 경우 | under fetch | 그외
    if R < start or end < L:
        return (-1, -1)
    if L <= start and end <= R:
        return tree[node]
    mid = (start + end) // 2
    ltree = query(node * 2, start, mid, L, R)
    rtree = query(node * 2 + 1, mid + 1, end, L, R)

    if ltree[1] == -1:
        return rtree
    elif rtree[1] == -1:
        return ltree
    else:
        if ltree[0] > rtree[0]:
            return rtree
        else:
            return ltree


# 재귀를 사용하는 쿼리를 또 재귀적으로 사용한다. 🔨
# w가 줄면 h는 적어도 커져야 하므로, 최소값의 인덱스 기준으로 좌우로 쪼갠다.
def getMax(L, R):
    # 현재 범위에서 너비를 구해 | 왼쪽 오른쪽으로 나눠서 또 너비를 구해봐
    h, h_idx = query(1, 0, len(arr) - 1, L, R)
    area = (R - L + 1) * h

    if L <= h_idx - 1:
        tmp_area = getMax(L, h_idx - 1)
        area = max(area, tmp_area)

    if h_idx + 1 <= R:
        tmp_area = getMax(h_idx + 1, R)
        area = max(area, tmp_area)

    return area


while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    arr = data[1:]
    tree = [0 for _ in range(len(arr) * 4)]
    init(1, 0, len(arr) - 1)
    print(getMax(0, len(arr) - 1))


"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0

7 2 1 4 5 1 3 3
0
"""