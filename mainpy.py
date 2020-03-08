import sys
import copy


def input(): return sys.stdin.readline().rstrip()


def moveDice(res, di):  # 주사위와 di 방향
    arr = copy.deepcopy(res)
    if di == 1:  # 0 1 2 3 4 5 -> 0 5 2 4 1 3
        arr[0] = res[0]
        arr[1] = res[5]
        arr[2] = res[2]
        arr[3] = res[4]
        arr[4] = res[1]
        arr[5] = res[3]
    elif di == 2:  # 0 1 2 3 4 5 -> 0 4 2 5 3 1
        arr[0] = res[0]
        arr[1] = res[4]
        arr[2] = res[2]
        arr[3] = res[5]
        arr[4] = res[3]
        arr[5] = res[1]
    elif di == 3:  # 0 1 2 3 4 5 -> 3 0 1 2 4 5
        arr[0] = res[3]
        arr[1] = res[0]
        arr[2] = res[1]
        arr[3] = res[2]
        arr[4] = res[4]
        arr[5] = res[5]
    elif di == 4:  # 0 1 2 3 4 5 -> 1 2 3 0 4 5
        arr[0] = res[1]
        arr[1] = res[2]
        arr[2] = res[3]
        arr[3] = res[0]
        arr[4] = res[4]
        arr[5] = res[5]
    return arr


(N, M, x, y, k) = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
cmd = list(map(int, input().split()))


dice = [0]*(6)  # 0,1,2,3,4,5
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 명령어의 수만큼 -> 이동한다 : 주사위를 먼저 이동사키고
for cm in cmd:
    nx = x + dx[cm-1]
    ny = y + dy[cm-1]
    if(nx < 0 or nx >= N or ny < 0 or ny >= M):
        continue
    dice = moveDice(dice, cm)
    x = x + dx[cm-1]
    y = y + dy[cm-1]
    # 이동한 칸에 수가 0 이면 주사위 바닥면 복사
    if(board[x][y] == 0):
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    # 0이 아니라면 보트판의 수가 주사위 바닥면 복사 및 보드판 0
    print(dice[3])
    print("-->", dice)
    # 주사위 상단 출력
