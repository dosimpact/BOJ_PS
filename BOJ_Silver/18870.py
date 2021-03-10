
N = int(input())
data = list(map(int, input().split()))
data_set = list(set(data))
data_set.sort()
data_dict = dict()
for i, d in enumerate(data_set):
    data_dict[d] = i


print(*list(map(lambda x: data_dict[x], data)))
