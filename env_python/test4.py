from itertools import combinations


for i in range(5):
    print(list(combinations(range(4), i)))  # [0,1,2,3] , 0,1,2,3,4
