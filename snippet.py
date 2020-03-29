from collections import deque

# 1초동안 움직일 수 있는 모든 경우


def move(cor1, cor2, board):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ret = []
    # 이동
    for m in move:
        if board[cor1[0]+m[0]][cor1[1]+m[1]] == 0 and board[cor2[0]+m[0]][cor2[1]+m[1]] == 0:
            ret.append({(cor1[0]+m[0], cor1[1]+m[1]),
                        (cor2[0]+m[0], cor2[1]+m[1])})

    rotate = [1, -1]
    # 가로회전
    if cor1[0] == cor2[0]:
        for r in rotate:
            if board[cor1[0]+r][cor1[1]] == 0 and board[cor2[0]+r][cor2[1]] == 0:
                ret.append({(cor1[0]+r, cor1[1]), (cor1[0], cor1[1])})
                ret.append({(cor2[0]+r, cor2[1]), (cor2[0], cor2[1])})
    # 세로회전
    else:
        for r in rotate:
            if board[cor1[0]][cor1[1]+r] == 0 and board[cor2[0]][cor2[1]+r] == 0:
                ret.append({(cor1[0], cor1[1]), (cor1[0], cor1[1]+r)})
                ret.append({(cor2[0], cor2[1]), (cor2[0], cor2[1]+r)})
    return ret


def solution(board):
    size = len(board)
    # 경계 체크 쉽게하기 위해서 지도의 상하좌우에 1 추가
    new_board = [[1 for i in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = board[i][j]

    que = deque()
    visited = []

    # queue에 [로봇의 좌표정보, 지금까지 거리] 형태로 넣음
    que.append([{(1, 1), (1, 2)}, 0])
    visited.append({(1, 1), (1, 2)})

    while len(que) != 0:
        temp = que.popleft()
        cor = list(temp[0])  # {()()} set형태 > list 전환 왜 ?
        dist = temp[1]+1
        print(cor)
        for m in move(cor[0], cor[1], new_board):  # [ {(),()}, ]
            if (size, size) in m:  # 해당 set안에 원하는 좌표가 있는경우
                return dist

            if not m in visited:  # [ {(),() } , ... ]
                que.append([m, dist])
                visited.append(m)

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
