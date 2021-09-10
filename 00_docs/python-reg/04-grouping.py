import re

# ✅ 그루핑 ( )
# ABC 문자열이 계속해서 반복되는지 여부를 조사하고 싶다.
# eg) ABC --- ok
# eg) ABCABCABC ---ok

print(re.sub("(ABC)", "*", "ABCA"))
# *A
print(re.sub("(ABC)", "*", "ABC"))
#  *
print(re.sub("(ABC)", "*", "ABCABC"))
#  **

# ✅ eg) 그룹핑에서 문자열 뽑기
# 아래 예시는 전체가 매핑되어 *으로 바뀐다.
# 여기서 이름부분만 추출하고 싶다.
print(re.sub(r"(\w)+\s+\d+[-]\d+[-]\d+", "*", "PARK 010-4691-1247"))
#  *
m = re.search(r"(\w+)\s+\d+[-]\d+[-]\d+",  "PARK 010-4691-1247")
print(m)  # <re.Match object; span=(0, 18), match='PARK 010-4691-1247'>
print(m.start())  # 0
print(m.end())  # 18
print(m.span())  # (0, 18)
print(m.group())  # PARK 010-4691-1247
print(m.group(1))  # PARK
# print(m.group(2))  # ERROR

m = re.search(r"(\w+)\s+((\d+)[-]\d+[-]\d+)", "PARK 070-1234-5678")
print(m.group())   # 매칭 결과
# PARK 010-1234-5678
print(m.group(1))  # 이름
# PARK
print(m.group(2))  # 전화 번호
# 070-1234-5678
print(m.group(3))  # 국번
# 070
