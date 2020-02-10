# 순열 조합 정리 permutations combinations import itertools

import itertools

pool = ['A', 'B', 'C']

# 결과는 튜플로 반환된다. -> join을 통해 하나의 문자열로 뭉처줄 수 있다.

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(list(itertools.permutations(pool)))

#['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
#['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기

# [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.combinations(pool, 2)))
# ['ABC']
print(list(map(''.join, itertools.combinations(pool, 3))))  # 3개의 원소로 수열 만들기
#['AB', 'AC', 'BC']
print(list(map(''.join, itertools.combinations(pool, 2))))  # 2개의 원소로 수열 만들기
