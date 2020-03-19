"""

a 버튼은 2번버튼을 1번
b 버튼은 2번 버튼을 2번
{'a': [2, 1], 'b': [2, 2], 'c': [2, 3], 'd': [3, 1], 'e': [3, 2], 'f': [3, 3], 'g': [4, 1], 'h': [4, 2], 'i': [4, 3], 'j': [5, 1], 'k': [5, 2], 'l': [5, 3], 'm': [6, 1], 'n': [6, 2], 'o': [6, 3], 'p': [7, 1], 'q': [7, 2], 'r': [7, 3], 's': [7, 4], 't': [8, 1], 'u': [8, 2], 'v': [8, 3], 'w': [9, 1], 'x': [9, 2], 'y': [9, 3], 'z': [9, 4]}
"""


import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = False
btn = {}

p, w = map(int, input().split())
msg = list(input())
counter = 2
al = ord('a')
for e in [3, 3, 3, 3, 3, 4, 3, 4]:
    for j in range(e):
        btn[chr(al)] = [counter, j+1]
        al += 1
    counter += 1

if DEBUG:
    print(btn)
    print(msg)

ans = 0
beforebtnNum = 0
for m in msg:
    if m == ' ':  # 현재가 공백인 경우
        ans += p
        beforebtnNum = 0
    else:
        nowAlpha = m.lower()
        if beforebtnNum == btn[nowAlpha][0]:  # 같은 버튼이라면 기다리는 시간 추가
            ans += w
        ans += p * btn[nowAlpha][1]
        beforebtnNum = btn[nowAlpha][0]
print(ans)

# 그 전에 누를 버튼이랑,
"""
2 10
ABBAS SALAM
"""
