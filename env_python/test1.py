

# 가정 0,1,...9 까지 집합 표현.

# 공집합
# print(0)  # 0
# print(bin(0))  # 0
# 전체 집합
U = (1 << 10)-1
# print(U)
# print(bin(U))  # 0b1111111111

data = 570  # 1 3 4 5 9
print(data, bin(data))  # 570 0b1000111010

# 존새성 : AND
res = data & 1 << 1  # 1이 존재하니?
print(res)  # 2 , True
res = data & 1 << 2  # 2가 존재하니?
print(res)  # 0 , False

# 추가 : OR
data = data | 1 << 2  # 2 추가
print(data, bin(data))  # 574 0b1000111110
res = data & 1 << 2  # 2가 존재하니?
print(res)  # 4 , True

# 제거
data = data & ~(1 << 2)  # 2 제거
print(data, bin(data))  # 570 0b1000111010
res = data & 1 << 2  # 2가 존재하니?
print(res)  # 0

# 업데이트 (토글)
data = data ^ (1 << 2)  # 2 토글( 0 > 1 )
print(data, bin(data))  # 574 0b1000111110
res = data & 1 << 2  # 2가 존재하니?
print(res)  # 4 , True
