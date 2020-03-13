"""
후보 추천하기 문제 리팩토링
- 정렬하는 함수 다시 이용해 보고 ( 디폴트 = 오름차 = 앞 - 뒤 (자연스러운 위치 ) 
-
fb) map이랑 , filter같은 경우 list형이 아니다, list로 받거나 바꾸거나.
"""
import sys
import functools


def input(): return sys.stdin.readline().rstrip()


def cmp(x, y):
    if x[1] == y[1]:
        return y[2]-x[2]
    else:
        return y[1] - x[1]


# 입력 사진틀  총 추천 횟수 추천받은 순서
piclen = int(input())
reclen = int(input())
reclist = list(map(int, input().split()))

pics = []  # [ 누구,추천수,언제 ] #주의 pics의 인덱스는 큰 의미가 없고 단지 사진 갯수


for i, rec in enumerate(reclist):
    now = rec

    tmp = list(filter(lambda x: x[0] == now, pics))

    if(tmp):  # 해당 후보가 사진에 있는경우
        idx = pics.index(tmp[0])
        pics[idx][1] += 1
    else:  # 없는경우
        if len(pics) < piclen:  # 사진이 남는경우
            pics.append([now, 1, i])
        else:  # 안남는 경우
            # 정렬 -> 1.추천수 많은순 내림차 2. 게시된 지 가장 최근순 [2] => 내림차
            pics = sorted(pics, key=functools.cmp_to_key(cmp))
            pics.pop(len(pics)-1)
            pics.append([now, 1, i])
# print(pics)
ans = []
for pic in pics:
    ans.append(pic[0])
ans.sort()
for an in ans:
    print(an, end=" ")
