from itertools import combinations, permutations, product

# [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]


def solution(dices):
    Njari = len(dices)  # 3
    availJarisu = set()
    for dice in dices:
        for e in dice:
            availJarisu.add(e)
    print(availJarisu)
    for i in range(1, Njari+1):  # 1,2,3
        pass


print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))
# 주사위 N개 1개만 골라도 된다.. ㅅㅂ
