"""
2966
"""


import sys


def input(): return sys.stdin.readline().rstrip()


N, Ans = int(input()), list(input())

Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B']
score = [0, 0, 0]

for Ans_i, Ans_e in enumerate(Ans):
    if Adrian[Ans_i % len(Adrian)] == Ans_e:
        score[0] += 1
    if Bruno[Ans_i % len(Bruno)] == Ans_e:
        score[1] += 1
    if Goran[Ans_i % len(Goran)] == Ans_e:
        score[2] += 1

winnerScore = max(score)
print(winnerScore)

if score[0] == winnerScore:
    print("Adrian")
if score[1] == winnerScore:
    print("Bruno")
if score[2] == winnerScore:
    print("Goran")

# winnerNames = []
# for scoreIdx, scoreE in enumerate(score):
#     if scoreE == winnerScore:
#         name = ''
#         if scoreIdx == 0:
#             name = "Adrian"
#         elif scoreIdx == 1:
#             name = "Bruno"
#         else:
#             name = "Goran"
#         winnerNames.append(name)


# for winnerName in winnerNames:
#     print(winnerName)

"""
리팩토링

1. 리스트의 인덱스를 고를때 
[] 으로 고르는데 -> 인덱

2. 입력줄때


N, Ans = int(input()), list(input()) 이렇게 튜플 형태로 해도 된다. 더 읽기 좋잖아

3. 최고점자 출력할때.

왜 구지 최고점자를 따로 모아서, 출력을하려함 ?
그냥 바로바로 점수 최고인지 보고 출력해.

"""
