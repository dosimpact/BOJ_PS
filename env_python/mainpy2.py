import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 모든 사진 틀은 비어 있음
# 추천시 게시,
# 비어있는 사진 틀이 없다 - 추천받은 횟수 가장 적은 학생 사진 삭제
# 동점자 ? - 가장 오래된 사람 제거
# 이미 게시된 경우 - 추천 횟수 증가
# 삭제 되는 경우 추천 횟수 리셋
# 최종 후보 오름차 출력

# 추천수,게시순서,학생번호
N = int(input())
M = int(input())
data = list(map(int, input().split()))
d = dict()

for idx, t in enumerate(data):
    if t in d:  # 있음 ❌ 있는것을 먼저 체크
        d[t][0] += 1
    elif len(d.keys()) < N:  # 빈 액자
        d[t] = [1, idx]
    else:  # 제거
        wridx = sorted(zip(d.values(), d.keys()),
                       key=lambda x: (x[0][0], x[0][1]))
        # print(f"wridx {wridx}")
        del d[wridx[0][1]]
        d[t] = [1, idx]

print(*sorted(d.keys()))

"""
❌
3
7
1 2 2 3 3 3 4 5 6

3
9
2 1 4 3 5 6 2 7 2

3
6
1 2 3 1 2 3
>1 2 3

3
3
1 1 1
>1

3
7
1 2 3 3 2 1 4 5 6
>2 3 6


"""
