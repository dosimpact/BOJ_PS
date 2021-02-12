import heapq


arr = [-4, -1, -5, -3, -8, -6, -3]
print(arr)
heapq.heapify(arr)
print(arr)
print(arr[0])


heapq.heappush(arr, 2)
print(arr)
while arr:
    print(heapq.heappop(arr))
