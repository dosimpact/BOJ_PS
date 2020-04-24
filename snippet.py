
"""
힙 자료 구조 

"""
import heapq

arr = [4, 1, 5, 3, 8, 6, 3, 9953, 12, 43, 555]

print(arr)  # [4, 1, 5, 3, 8, 6, 3, 9953, 12, 43, 555]
heapq.heapify(arr)
print(arr)  # [1, 3, 3, 4, 8, 6, 5, 9953, 12, 43, 555]
print(arr[0])  # 가장 작은 원소 보장, 그외는 아니다.

heapq.heappush(arr, 2)

print(heapq.heappop(arr))  # 1
print(heapq.heappop(arr))  # 2
print(heapq.heappop(arr))  # 3
print(heapq.heappop(arr))  # 3
print(heapq.heappop(arr))  # 4
print(heapq.heappop(arr))  # 5
print(heapq.heappop(arr))  # 6
print(arr)  # [8, 12, 555, 9953, 43]
