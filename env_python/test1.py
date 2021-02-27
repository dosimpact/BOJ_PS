import sys

sys.stdin.readline

S = input().strip()

# 데이터 파싱
data = []
isMinus = False
num = ""
while S:
    # -,+ 인경우 : data에 넣고, 새로 시작
    if S[0] in ["+", "-"]:
        data.append(int(num))
        num = ""
        num += S[0]
        S = S[1:]
    # 숫자인 경우 이어붙어
    else:
        num += S[0]
        S = S[1:]
    # 마지막 숫자 너히
data.append(int(num))
isMinus = False
ans = 0
for d in data:
    if d < 0:
        isMinus = True
    if isMinus:
        ans += -abs(d)
    else:
        ans += d

print(ans)
"""
55-50+40
-35

1+1-10
-8

0+0-0
0

9+9-9
9

9-9-9
-9
"""
