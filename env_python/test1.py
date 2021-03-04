from typing import *
# 이진 탐색 재귀 구현


def BSearch(arr: List[int], left: int, right: int, target: int):
    if left > right:
        return -1
    mid = (left+right)//2
    if arr[mid] == target:  # mid 가 답인경우 | 아닌 경우
        return mid
    elif arr[mid] < target:  # 좀 더 오른쪽으로 기울어야 한다.
        return BSearch(arr, mid+1, right, target)
    else:
        return BSearch(arr, left, mid-1, target)


data = [5, 1, 3, 7, 9]
data.sort()

# 숫자가 있는 경우 , 없는 경우
resIdx = BSearch(data, 0, len(data)-1, 7)  # 7을 찾을래
print(f"결과-Idx : {resIdx} (-1 Not Found)")

resIdx = BSearch(data, 0, len(data)-1, 8)  # 8을 찾을래
print(f"결과-Idx : {resIdx} (-1 Not Found)")

# 끝점인 경우
resIdx = BSearch(data, 0, len(data)-1, 1)
print(f"결과-Idx : {resIdx} (-1 Not Found)")

resIdx = BSearch(data, 0, len(data)-1, 9)
print(f"결과-Idx : {resIdx} (-1 Not Found)")


# 끝점을벗어난 경우
resIdx = BSearch(data, 0, len(data)-1, -20)  #
print(f"결과-Idx : {resIdx} (-1 Not Found)")

resIdx = BSearch(data, 0, len(data)-1, 9999)  #
print(f"결과-Idx : {resIdx} (-1 Not Found)")
