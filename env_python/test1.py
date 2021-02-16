import heapq

data = [(3, 2), (4, 2), (2, 3), (9, 3), (6, 3),
        (3, 2), (8, 4), (10, 2), (10, 3)]
print(data)
heapq.heapify(data)
print(data)
data = list(filter(lambda x: x[1] != 2, data))
print(data)
while data:
    print(heapq.heappop(data))
