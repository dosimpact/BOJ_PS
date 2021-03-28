from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


# 높이가 서로 다른 직사각형들
# 가장 큰 넓이의 직사각형을 구하시오
# 세그먼트 트리

# 요청 : 해당 구간에서 가장 작은 높이는 ? 그리고 그 인덱스는?
# 초기화 : 해당 구간에서 가장 작은 높이와 인덱스를 저장
# 답구하는 과정 : 특정구간에서 구해
# 그리디하게 - 가장 작은 녀석을 뺀 좌우 범위에서 또 더큰 사각형이 나올 수 있다.
arr = None
tree = None

# 구간의 높이 출력
def init(node, start, end):
    # backpropa, 구간의 최소 높이,인덱스
    if start == end:
        tree[node] = (arr[start], start)
        return tree[node]
    mid = (start + end) // 2
    ltree = init(node * 2, start, mid + 1)
    rtree = init(node * 2 + 1, mid + 1, end)
    if ltree[0] < rtree[0]:
        tree[node] = rtree
    else:
        tree[node] = ltree
    return tree[node]


# 구간의 노드값 요청
def query(node, start, end, L, R):
    # 범위 밖| 오버패칭 | 그외
    if R < start or end < L:
        return (-1, -1)
    if L <= start and end <= R:
        return tree[node]

    mid = (start + end) // 2
    ltree = query(node * 2, start, mid)
    rtree = query(node * 2, mid + 1, end)
    if ltree[0] == -1:
        return rtree
    elif rtree[0] == -1:
        return ltree
    else:
        if ltree[0] > rtree[0]:
            return rtree
        else:
            return ltree


def getMax(L, R):
    h, h_idx = query(1, 0, len(arr) - 1, L, R)
    area = h * (R - L + 1)
    # 분할 및 정복
    return area


while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    tree = [0 for _ in range(n * 4)]
    init(1, 0, len(arr) - 1)
    print(getMax(0, len(arr) - 1))

"""
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
"""