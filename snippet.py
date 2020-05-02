import heapq


ts = [(4, 5), (6, -7), (6, -252), (6, -100), (1, 1), (2, 1), (3, 1)]  # t, w
heapq.heapify(ts)

print(ts)
while ts:
    print(heapq.heappop(ts))
