N = int(input())
array = [0 for i in range(N+1)]  # 만약 N이 10이면 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, N+1):
    if (i % 3 == 0 and i % 2 == 0):
        array[i] = min(array[i//3], array[i//2], array[i-1]) + 1
        continue
    elif (i % 3 == 0 and i % 2 != 0):
        array[i] = min(array[i//3], array[i-1]) + 1
        continue
    elif (i % 3 != 0 and i % 2 == 0):
        array[i] = min(array[i//2], array[i-1]) + 1
        continue
    else:
        array[i] = array[i-1] + 1

print(array[N])
