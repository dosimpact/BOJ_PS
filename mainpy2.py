<<<<<<< HEAD
import sys


def input(): return sys.stdin.readline()

"""
이렇게 풀면 안되

해당 위치에서 5개  > -> 위로 아래로 다 내려가봐야되, 그래서 총 5개가 되어야함.
20*20*8
"""


def inRange(i, j):
    return (i >= 0 and j >= 0 and i < L and j < L)


def check(i, j, board):
    #print(f"check entry {i} {j} {board[i][j]} ")
    if board[i][j] == 0:
        return 0
    for di in [[(0, 1), (0, -1)], [(1, 1), (-1, -1)], [(1, 0), (-1, 0)], [(1, -1), (-1, 1)]]:
        # 현재 보드에서, di 방향으로 같은 색 갯수를 구할거임
        #print(f"check entry {i} {j} {board[i][j]} ")
        color = board[i][j]
        cnt = 1

        x, y = i + di[0][0], j + di[0][1]
        while inRange(x, y) and color == board[x][y]:
            cnt += 1
            x, y = x+di[0][0], y+di[0][1]

        if cnt == 5:
            x, y = i + di[1][0], j + di[1][1]
            if board[i][j] == board[x][y]:
                return 0
            else:
                return color
        # while inRange(x, y) and color == board[x][y]:
        #     cnt += 1
        #     x, y = x+di[1][0], y+di[1][1]
        # print(f"cnt : {cnt} > {i},{j}")
        # if cnt == 5:
        #     return color
    return 0


L = 19

board = [list(map(int, input().split())) for _ in range(L)]


# print("---")
# for b in board:
#     print(*b)

for i in range(L):
    for j in range(L):
        if board[i][j] == 0:
            continue
        res = check(i, j, board)
        if res == 1 or res == 2:
            print(res)
            print(i+1, j+1)
            exit(0)
        else:
            continue
print(0)
"""

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


0 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
=======
from collections import deque

# 1초동안 움직일 수 있는 모든 경우


def move(cor1, cor2, board):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ret = []
    # 이동 | 이동했을때, 0이라면 이동한다.
    for m in move:
        if board[cor1[0]+m[0]][cor1[1]+m[1]] == 0 and board[cor2[0]+m[0]][cor2[1]+m[1]] == 0:
            ret.append({(cor1[0]+m[0], cor1[1]+m[1]),
                        (cor2[0]+m[0], cor2[1]+m[1])})

    rotate = [1, -1]
    # 가로회전 ( ㅡ  > |  ) | 아래로 회전 2경우 ( 아래 둘다 0 | 추가 2번 )
    if cor1[0] == cor2[0]:
        for r in rotate:
            if board[cor1[0]+r][cor1[1]] == 0 and board[cor2[0]+r][cor2[1]] == 0:
                ret.append({(cor1[0]+r, cor1[1]), (cor1[0], cor1[1])})
                ret.append({(cor2[0]+r, cor2[1]), (cor2[0], cor2[1])})
    # 세로회전 ( | -> ㅡ ) | 위로 회전하는 2경 ( 위 둘다 0 | 추가 2번)
    else:
        for r in rotate:
            if board[cor1[0]][cor1[1]+r] == 0 and board[cor2[0]][cor2[1]+r] == 0:
                ret.append({(cor1[0], cor1[1]), (cor1[0], cor1[1]+r)})
                ret.append({(cor2[0], cor2[1]),  (cor2[0], cor2[1]+r)})
    return ret


def solution(board):
    size = len(board)
    # 경계 체크 쉽게하기 위해서 지도의 상하좌우에 1 추가
    new_board = [[1 for i in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = board[i][j]
    print(new_board)
    que = deque()
    visited = []

    # queue에 [로봇의 좌표정보, 지금까지 거리] 형태로 넣음
    que.append([{(1, 1), (1, 2)}, 0])
    visited.append({(1, 1), (1, 2)})  # 방문을 set형태로 넣네, 1단위 인가?

    while len(que) != 0:
        temp = que.popleft()
        cor = list(temp[0])  # 한단위 중 첫번쨰에 위치가 있다. , 두번쨰는 거리
        dist = temp[1]+1

        # 1유닛, 2유닛, 보드 > 해당 로봇의 상태에서 나올 수 있는 위치들을 모두 뽑아.
        # [ { (유닛1) (유닛2)  } ]  # 로봇의 위치는 상관없는듯
        for m in move(cor[0], cor[1], new_board):
            if (size, size) in m:  # 정답인 경우
                return dist

            if not m in visited:  # 해당 로봇의 조합을 안해본 경우.
                que.append([m, dist])
                visited.append(m)

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
      0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

"""
fb)
로봇이 두칸을 차지하지만, 1개의 노드로 봐야함.
>>>>>>> 6c9bce59587d3102dfdb55c0cf825cfb0ecfc81c

"""
