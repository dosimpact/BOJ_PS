# NM 게임 맵
# 내구도 있는 건물들이 있음
# 적군 HP 감소 - 0 이하시 파괴,
# 아군 HP 증가

# 공격, 회복 스킬은 , 정사각형 모양
# 스킬 [type, r1, c1, r2, c2, degree]
# type 1 공격, 2 회복 , 범위 .... , 정도


def changeBoard(board, Range, degree):
    r1, c1, r2, c2 = Range
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            board[i][j] += degree


def getPostiveBoard(board):
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                ans += 1
    return ans


def printBoard(board):
    for row in board:
        print(*row)


def rangeToList(Range, N, M):
    # 2차원 범위를 1차원 범위로 변경해주는 함수
    result = []
    r1, c1, r2, c2 = Range
    for i in range(r1, r2+1):
        result.append([c1 + (M*i), c2+(M*i)])
    return result


print(rangeToList((0, 0, 1, 1), 4, 4))


def solution(board, skill):
    for sk in skill:
        t, r1, c1, r2, c2, degree = sk
        if t == 1:
            changeBoard(board, (r1, c1, r2, c2), -degree)
        else:
            changeBoard(board, (r1, c1, r2, c2), degree)
    printBoard(board)
    return getPostiveBoard(board)


print(solution(
    [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [
        2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

))
