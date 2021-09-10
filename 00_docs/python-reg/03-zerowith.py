import re

# ✅ 메타문자 - 비소비형
# +,*,[],{} 등 메타문자는 매치되는 문자열의 위치가 변경된다.
# 그와 다르게 문자열의 위치가 변경되지 않는 ( 소비되지 않는 ) 메타 문자도 있다.
# ( zerowith assertions ) 라고 함


# | or 의 뜻
print(re.sub("red|black", "*", "red sky ~ "))
# red -> *

# ^ 은 맨 처음과 일치함을 의이
print(re.sub("^hello", "*", "hello world"))
# * world


# $ 는 문자열의 끝과 매치함을 의미
print(re.sub("world$", "*", "hello world"))
# hello *


# \b 는 단어 구분자 이다 ( whitespace ) 공백과 매칭된다.
print(re.sub(r"\bworld\b", "*", "hell world hell"))
# hell * hell
