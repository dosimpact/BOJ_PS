
import re
# ✅ eg) re.sub 는 문자열 치환이다.
#  패턴, 대처할 문자열, 대상 문자열
# print(re.sub("[a-z]", "-", "hello world"))
# ----- -----

# ✅ eg) [] + 범위(-)
# print(re.sub("[a-zA-Z]", "*", "hello 123"))
# ***** 123

# ✅ eg) [] + 여집합(^)
# 소문자가 아닌것들은 다 *로 바꾸기
# print(re.sub("[^a-z]", "*", "Hello Wor3d"))
# *ello**or*d

# ✅ eg) \d \w \s
# 공백을 제외하고 다 *로 표시하기
# 숫자 -> $, 숫자+문자 -> @, 공백 -> *
target = "Hello Worl3d"
# 숫자를 변경
target = re.sub("[\d]", "$", target)
print(target)  # Hello Worl$d
# 숫자+문자를 변경
target = re.sub("[\w]", "@", target)
print(target)  # @@@@@ @@@@$@
target = re.sub("[\s]", "*", target)
# 공백을 변경
print(target)  # @@@@@*@@@@$@
# print(re.sub("[\S]", "*", "Hello Wor3d"))


# ✅ eg) .(dot) 찾기
# [] 문자 클래스 안에 .을 넣으면 검색 가능
print(re.sub("[.]", " ", "...hello...world..."))
#    hello   world
# 혹은, r이라는 키워드를 이용해서, .자체를 표현하도록 이스케이프 문자와 표현하자.
print(re.sub(r"\.", " ", "...hello...world..."))
#    hello   world
