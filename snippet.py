from itertools import combinations, permutations


ori = [1, 2, 3]

res = list(permutations(ori, 2))
print(res)
res = set(res)
print(res)
