from math import ceil
import sys
from typing import *


def solution(board: List[List[int]], moves: List[int]):
    # moves 대로, 보드에서 원소를 하나씩 꺼낸다.
    # 바구니에 넣을때 그전의 원소랑 같으면 둘다 지운다.
    boardH = len(board)
    stack = []
    ans = 0
    for m in moves:
        c = m - 1
        r = 0
        while r < boardH:
            if board[r][c] != 0:
                tmp = board[r][c]
                board[r][c] = 0
                if stack and stack[-1] == tmp:
                    ans += 2
                    stack.pop(-1)
                else:
                    stack.append(tmp)
                break
            r += 1
    return ans

# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
# 어렵게 생각 X , 진행만 100이상이면 여러번 베포 가능


def solution(progresses: List[int], speeds: List[int]):
    daygo = 0
    ans = []
    check = [False for _ in range(len(progresses))]
    while progresses:
        daygo += 1
        tmp = 0
        while progresses and progresses[0]+speeds[0]*daygo >= 100:
            tmp += 1
            progresses.pop(0), speeds.pop(0), check.pop(0)
        if tmp != 0:
            ans.append(tmp)
    return ans


print(solution([99, 1], [1, 99]))
print(solution([93, 30, 55]	, [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))
print(solution([95, 99, 98, 99, 98]	, [1, 1, 1, 1, 1]))
print(solution([97, 99, 98, 99, 98]	, [1, 1, 1, 1, 1]))
