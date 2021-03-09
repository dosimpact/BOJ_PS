# from itertools import product, combinations
# graph, N, M = [[]], 1, 1

# # 1 -- 2차원 배열 필터 - 0인경우
# emptys = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 0]

# # 2 -- 2차원 배열 필터 - 1인경우
# viruss = list(filter(lambda x: graph[x[0]]
#                      [x[1]] == 1, product(range(N), range(M))))

# # 3 -- 2차원 배열 필터 - 2인경우
# walls = []
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 2:
#             walls.append((i, j))


from itertools import product, combinations

# for i in range(1,5):
# for j in range(6,10):
# print(i,j)

print(list(product([1, 2], [3, 4], [5, 6])))  # 3중 포문을 한번에~
graph = [[1, 0], [2, 0], [1, 1]]  # 3X2 의 2차원 배열이 되겠다.
zeros = [(i, j) for i in range(3) for j in range(2) if graph[i][j] == 0]
print(zeros)
zeros = list(filter(lambda x: graph[x[0]]
                    [x[1]] == 0, product(range(3), range(2))))
print(zeros)
