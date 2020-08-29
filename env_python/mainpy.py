import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


AGE = int(input())

MAX_HEART = 220 - AGE


def KIND_OF(per):
    if per < 60:
        return 0
    if per >= 60 and per < 68:
        return 1
    if per >= 68 and per < 75:
        return 2
    if per >= 75 and per < 80:
        return 3
    if per >= 80 and per < 90:
        return 4
    if per >= 90:
        return 5


now_kind = -1
counter = 0
ans = [0]*6
for line in sys.stdin:
    a = int(line)
    per = (a / MAX_HEART)*100
    ans[KIND_OF(per)] += 1
print(*ans[::-1])

"""
30
50
55
60
65
70
75
80
85
90
95
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
"""
