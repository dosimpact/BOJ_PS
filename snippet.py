from itertools import combinations, permutations


# a = 27

# b = 83

# print(a & b)
# print(a | b)
# print(a ^ b)

# c = 1
# print(c << 2)
# print(c << 3)
# print(c << 4)


# a = "0b000011011"
# b = "0b001010011"
# print(int(a, 2))
# print(int(b, 2))

# print(bin(27))
# print(bin(83))

# S = { 1,3,4,5,9} = 570

print(570 & (1 << 3))  # 8 응 있다.
print(570 | (1 << 2))  # 574 2가 추가 되었다.

# 단순히 - 를 붙여서 곤란하네....
print(574 | ~(1 << 2))  # -1 다른 연산결과!!

print(570 ^ (1 << 1))  # 568 1이 사라졌다.
