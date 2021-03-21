import sys
from collections import deque
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 모든 콘텐츠에, 하나의 장르가 태깅
# 선호도 0.0 ~5.0
# 열람 X를 먼저 추천 | 열람 했으나 끝까지 다 못본 콘텐츠를 선호도 순으로 추천
#  Y 안본거, O 보다만거, W 다본거
# A~E = 장르


# 그냥 정렬인데 ?

ans_list = []  # 안본거 | 선호도 | x순 | y순 이네.❌ ( y순  | x순)

prefer = list(map(float, input().split()))  # A B C D E
N, M = map(int, input().split())
state = [list(input().strip()) for _ in range(N)]
genre = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if state[i][j] == 'Y':  # 0 안본거
            ans_list.append(
                (0, prefer[ord(genre[i][j])-ord('A')], j, i, genre[i][j]))
        elif state[i][j] == 'O':  # 1 보다 만거
            ans_list.append(
                (1, prefer[ord(genre[i][j])-ord('A')], j, i, genre[i][j]))

ans_list.sort(key=lambda x: (x[0], -x[1], x[3], x[2]))

for ans in ans_list:
    print(f"{ans[4]} {ans[1]} {ans[3]} {ans[2]}")


"""
5.0 5.0 5.0 5.0 5.0
3 3
YYW
YWW
OOO
ABC
DCE
ABC

4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
DCE

>
장르,선호도,위치


"""
