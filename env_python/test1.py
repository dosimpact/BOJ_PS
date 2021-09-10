data = [1, 3, 5, 7, 9]
query = 10

start, end = 0, len(data)
while start != end:
    if query <= data[(start + end) // 2]:
        end = (start + end) // 2
    elif data[(start + end) // 2] < query:
        start = (start + end) // 2 + 1

print(start, "[ idx ] query : ", query)

