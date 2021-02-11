
# 메타 문자
# 메타문자란 - 특별한 의미를 부여해서, 특별한 용도로 사용하는 문자이다.
# eg) . ^ $ * + ? { } [ ] \ | ( )


# 문자 클래스 [ ]
# [abc]
# [0-5]는 [012345]와 동일
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자
# [^0-9]라는 정규 표현식은 숫자가 아닌 문자만

"""
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
"""

import re
p = re.compile("ab*")  # 해당 정규식 패턴 p 를 계속 사용하겠다.#

"""
# match()	    문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()     정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
"""

# match ( 처음부터 매치 조사 )

p = re.compile('[a-z]+')
m = p.match("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>
print(m.group())  # python - 그게 무엇인지
m = p.match("3 python")
print(m)  # None

print("-"*30)
# search ( 전체를 매치 조사 )

p = re.compile('[a-z]+')
m = p.search("python")
print(m)  # <re.Match object; span=(0, 6), match='python'>
print(m.group())  # python - 그게 무엇인지
m = p.search("3 python")
print(m)  # <re.Match object; span=(2, 8), match='python'>
print(m.group())  # python


print("-"*30)
# findall
result = p.findall("life is too short")
print(result)  # ['life', 'is', 'too', 'short']

print("-"*30)
# finditer
result = p.finditer("life is too short")
print(result)  # <callable_iterator object at 0x000001ED4CE95828>
for r in result:
    print(r)  # <re.Match object; span=(0, 4), match='life'>

"""
method	목적
group()	매치된 문자열을 돌려준다.
start()	매치된 문자열의 시작 위치를 돌려준다.
end()	매치된 문자열의 끝 위치를 돌려준다.
span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
"""

"""
>>> m = p.match("python")
>>> m.group()
'python'
>>> m.start()
0
>>> m.end()
6
>>> m.span()
(0, 6)
"""

# 문자열 치환

p = re.compile('(blue|white|red)')
res = p.sub('colour', 'blue socks and red shoes')  # 일치하는 문자를  colour 로 변환
print(res)
