
# ✅ eg) bitset을 이용한 집합 자료구조

# 가정 : 1,2,3 원소를 추가 삭제 해보자.
# 1 은, 0번 원소가 있다 =   아무것도 없는 상태라 약속
ALL_REMOVED = 1

# 초기화
data = 1

# 1추가 , 3추가
data = data | (1 << 1)
data = data | (1 << 3)
print(bin(data))  # 0b1011

# 2존재, 3존재
print(bool(data & (1 << 2)))  # False
print(bool(data & (1 << 3)))  # True

# 3제거
data = data & ~(1 << 3)
print(bool(data & (1 << 3)))  # False
