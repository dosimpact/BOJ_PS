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


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)
