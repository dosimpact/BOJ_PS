import re

# ✅ 파이썬 정규식 기본 함수
# sub()     패턴에 매치되는 문자열을 치환한다.
# -> replace 하고자 함

# match()	문자열의 **처음부터** 정규식과 매치되는지 조사한다.
# -> 시작부터 틀리면 볼 필요도 없다.

# search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다. (처음부터가 아닌 중간에도 맞으면 ok )
# -> 시작부터 틀리더라도, 중간에 매칭되면 OK!

# findall()	정규식과 매치되는 모든 문자열(substring)을 **리스트**로 돌려준다.
# -> 매칭되는 문자열만 검색할래

# finditer()	정규식과 매치되는 모든 문자열(substring)을 **반복 가능한 객체**로 돌려준다.
# -> 매칭 되는 문자열안에서 그룹핑을 한것을 다룰래

print(re.findall("[\w]*[0-9][\w]*", " hel5lo wor3d hell haha"))
# ['hel5lo', 'wor3d']

# ✅ 파이썬 정규식 객체
# group()	매치된 문자열을 돌려준다.
# start()	매치된 문자열의 시작 위치를 돌려준다.
# end()	매치된 문자열의 끝 위치를 돌려준다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
#  ------------------------
# + eg) 그룹핑에서 문자열 뽑기
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
