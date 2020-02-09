# 나머지 연산의 개념 => 양수는 직관적인데, 음수는 -1이 가르키는 배열이 마지막 배열임을 안다면 별거없다.
"""
0   1   2   3   4    <- 배열 길이 : 5

0   1   2   3   4
5   6   7   8   ...

-5  -4  -3  -2  -1
..  -9  -8  -7  -6

"""

var = [0, 1, 2, 3, 4]

print(len(var))  # 길이 5

print(0 % len(var))  # 0 ~ 4
print(1 % len(var))
print(2 % len(var))
print(3 % len(var))
print(4 % len(var))

print(5 % len(var))  # 0 ~ 4
print(6 % len(var))
print(7 % len(var))
print(8 % len(var))
print(9 % len(var))

print(-1 % len(var))  # 4 ~ 0
print(-2 % len(var))
print(-3 % len(var))
print(-4 % len(var))
print(-5 % len(var))


print(-6 % len(var))  # 4 ~ 0
print(-7 % len(var))
print(-8 % len(var))
print(-9 % len(var))
print(-10 % len(var))
