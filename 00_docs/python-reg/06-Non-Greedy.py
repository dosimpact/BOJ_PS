import re

# ✅ Non-Greedy 옵션
# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용할 수 있다.
# eg) 태그를 선택하기

# 모든 문자를 소비해버린 경우
print(re.findall(r"<.*>", '<html><head><title>Title</title>'))
# ['<html><head><title>Title</title>']

# 모든 문자를 소비해버린 경우
# Quantifier + Lazy 을 이용해서 , 최소한의 문자만 소비하도록  한다.
print(re.findall(r"<.*?>", '<html><head><title>Title</title>'))
# ['<html>', '<head>', '<title>', '</title>']
