import re

# ✅ 전방 탐색 (?= )
# 소비되지 않는 메타문자 이다.

m = re.search(r".+(?=:)", "http://google.com")
print(m.group())  # http
m = re.search(r".+(?=:)", "h:ttp://google.com")
print(m.group())  # http


print(re.findall(r".+(?=:)", "http://google.com"))
#  ['http']


# \w는 alphanum 만 가능하다. :/. 은 제외되기 때문에 3개의 토큰이 나온다.
print(re.findall(r"\w+(?=:)", "h:ttp://goog:le.com"))
# ['h', 'ttp', 'goog']

# . 은 행넘김이 되지 않는다면(왠만하면) 다 매칭 하기 때문에
# 결국 하나로 합쳐진 1개의 토큰이 나온다?!
print(re.findall(r".+(?=:)", "h:ttp://goog:le.com"))
#  ['h:ttp://goog']

# ✅ eg) 행넘김(\n) 으로 구분하기
# 행넘김을 제외한 모든 문자는 . 이다. .을 이용해서 findall 하면 구분 가능
print(re.findall(r".+", """sentence1\nsent\tenc\te2"""))
# ['sentence1', 'sent\tenc\te2']

# ✅ 부정형 전방 탐색 (?! )
# eg) .bat 파일 제외
# .*[.](?!bat).*$

# (조건,비소비 메타문자) : (?!bat) bat 이 아닌것이라면 선택하도록 함
# (조건,비소비 메타문자) : $ 끝나는 지점이라면 선택하도록 함

# (소비 메타문자)  .*[.] : (개행 제외 0개 이상의 문자). 을 고르도록 한다.
# (소비 메타문자)  .*    : (개행 제외 0개 이상의 문자)  을 고르도록 한다.

print(re.findall(r".*[.](?!bat).*$", "test.exe"))
# ['test.exe']
print(re.findall(r".*[.](?!bat).*$", "test.bat"))
# []
