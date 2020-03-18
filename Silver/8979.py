

import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = False
n, k = map(int, input().split())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, input().split())))
nlist.sort(key=lambda x: (-x[1], -x[2], -x[3]))
idx = [n[0] for n in nlist].index(k)
while idx > 0 and nlist[idx][1:] == nlist[idx-1][1:]:
    idx -= 1

print(idx+1)

"""
fb) 매개변수 타입지정 
def test(me: [], you: []):
    print(me, you)  # [1, 2] [3, 4]


test([1, 2], [3, 4])

fb) 국가 코드가 1,2,3,4 순서대로만 주어지는게 아닌데, 순서대로 받는것 처럼 함


fb) 리펙토링 생각해보니까, N제곱으로 풀었네, N만을 풀자.

1.정렬

2.해당 인덱스 구하기

3.앞에 같은 동점자 녀석이 있으면 그만큼 idx 감소
"""
"""
올림픽

금메달 수가 더 많은 나라
금메달 수가 같으면, 은메달 수가 더 많은 나라
금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라


정렬을 써도 되는데, 공동 등수때문에, 하나하나 비교를 하자.
"""


def input(): return sys.stdin.readline().rstrip()


def isWinORSame(me: [], you: []):
    if me[0] == you[0]:
        if me[1] == you[1]:
            if me[2] == you[2]:
                return True
            else:
                return me[2] - you[2] > 0
        else:
            return me[1] - you[1] > 0
    else:
        return me[0] - you[0] > 0


n, k = map(int, input().split())
grade = [1]*n
nlist = []

for _ in range(n):
    nlist.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if isWinORSame(nlist[i][1:], nlist[j][1:]):
            pass
        else:
            grade[i] += 1


for i, e in enumerate(nlist):
    if e[0] == k:
        print(grade[i])

"""
fb) 매개변수 타입지정 
def test(me: [], you: []):
    print(me, you)  # [1, 2] [3, 4]


test([1, 2], [3, 4])

fb) 국가 코드가 1,2,3,4 순서대로만 주어지는게 아닌데, 순서대로 받는것 처럼 함


fb) 리펙토링 생각해보니까, N제곱으로 풀었네, N만을 풀자.

1.정렬

2.해당 인덱스 구하기

3.앞에 같은 동점자 녀석이 있으면 그만큼 idx 감소
"""
