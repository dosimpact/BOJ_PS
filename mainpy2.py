

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
