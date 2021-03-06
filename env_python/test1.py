

# 세그먼트 트리

# 기능
# 1.세그먼트 트리 만들기 (init)
# 2.update
# 3.sum

# 탐색
# - 루트 노드는 인덱스 1부터 시작
# 노드의 인덱스가 K 라면 왼쪽은 K*2 , 오른쪽은 K*2+1 이다.

# 시간 복잡도
# 숫자 검색 =  logN
# 숫자 업데이트 = logN

# 공간 복잡도
# (최선) 3**2 < 12 < 4**2 라면 > (4**2) * 2 가 트리 크기
# (차선) tree배열 크기 = N*4

import math
import sys
sys.setrecursionlimit(10**6)
# N = 12 (12 숫자의 구간합을  구해보자)
arr = [3, 5, 6, 7, 2, 9, 4, 5, 2, 8, 1, 5]
h = int(math.ceil(math.sqrt(len(arr))))  # log12 = 3.xx -> 4
tree_size = (1 << (h+1))  # 2**5
tree = [0 for _ in range(tree_size+1)]
print("height", h)
print("tree_size", tree_size)

# tree의 idx는 node가 담당, arr의 idx는 start,end 이다.


def seg_init(node: int, start: int, end: int):  # [start,end]를 초기화 하고 싶다.
    # print(f"node,start,end : {node,start,end}")
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = seg_init(node*2, start, mid) + seg_init(node*2+1, mid+1, end)
    return tree[node]


seg_init(1, 0, 11)
print(tree)
# [0, 57, 32, 25, 14, 18, 11, 14, 8, 6, 9, 9, 9, 2, 9, 5, 3, 5, 0, 0, 7, 2, 0, 0, 4, 5, 0, 0, 8, 1, 0, 0, 0]

# 재귀변수 node,start,end
# idx의 변수를 바꾸었고, 그 차이는 diff이다.


def seg_update(node: int, start: int, end: int, idx: int, diff: int):
    # 특정 leaf 노드르 값을 바꾸는 경우 - 범위에 관련된 노드가 update
    if not(start <= idx and idx <= end):  # basecase  - out of idx
        return
    tree[node] += diff
    if start == end:  # basecase - leaf node
        return
    mid = (start+end)//2
    seg_update(node*2, start, mid, idx, diff)
    seg_update(node*2+1, mid+1, end, idx, diff)
    return


arr[0] = 10
seg_update(1, 0, 11, 0, 7)  # 0~11을 가지는 root 노드부터 전파,( 0번을 +7 했다.)
print(tree)
"""
[0, 57, 32, 25, 14, 18, 11, 14, 8, 6, 9, 9, 9, 2, 9, 5, 3, 5, 0, 0, 7, 2, 0, 0, 4, 5, 0, 0, 8, 1, 0, 0, 0]
[0, 64, 39, 25, 21, 18, 11, 14, 15, 6, 9, 9, 9, 2, 9, 5, 10, 5, 0, 0, 7, 2, 0, 0, 4, 5, 0, 0, 8, 1, 0, 0, 0]
"""

# node-start-end 에서
# 쿼리 LR 의 합을 구하고자 한다.
# 특정 노드 -- 쿼리 :
"""
# 1. 전혀 상관없는 경우
# 2. 해당 노드에서 알 수 있는 정보보다, 요청사항이 많은경우
    - 우선 노드 정보를 다 주자.
# 3. 해당 노드에서 알 수 있는 정보보다, 요청사항이 적은 경우
    - 다음 노드들에게 맡기자.
"""


def seg_sum(node: int, start: int, end: int, L: int, R: int):
    if (end < L)or(R < start):  # basecase - 1
        return 0
    if L <= start and end <= R:  # basecase - 2
        return tree[node]
    mid = (start + end)//2  # basecase - 3
    return seg_sum(node*2, start, mid, L, R) + seg_sum(node*2+1, mid+1, end, L, R)


# arr = [3+7, 5, 6, 7, 2, 9, 4, 5, 2, 8, 1, 5]
print(f"[0,0]의 합 : {seg_sum(1,0,11,0,0)}")
print(f"[0,1]의 합 : {seg_sum(1,0,11,0,1)}")
print(f"[0,2]의 합 : {seg_sum(1,0,11,0,2)}")
print(f"[0,3]의 합 : {seg_sum(1,0,11,0,3)}")

print(f"[1,8]의 합 : {seg_sum(1,0,11,1,8)}")
print(f"[2,8]의 합 : {seg_sum(1,0,11,2,8)}")
print(f"[3,8]의 합 : {seg_sum(1,0,11,3,8)}")
print(f"[4,8]의 합 : {seg_sum(1,0,11,4,8)}")
