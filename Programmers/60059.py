"""

. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,

key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.

"""

import copy

DEBUG = True


def rotateCW(s: []):
    res = copy.deepcopy(s)
    L = len(s)
    for i in range(L):  # 0 1 2
        for j in range(L):
            res[j][(L-1)-i] = s[i][j]  # 0 1 2, 3 2 1
    return res


def solution(key, lock):
    # key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    # lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    N = len(lock)
    M = len(key)
    cntInit = 0
    for loc in lock:
        cntInit += loc.count(0)

    ans = False

    for _ in range(4):
        for i in range(-M+1, N):
            for j in range(-M+1, N):
                # 해당 좌표에서 시도해 본다.
                cnt = cntInit
                keeptrying = True
                # 키를 상대 좌표로 돕니다.
                for kx in range(0, M):
                    for ky in range(0, M):
                        (x, y) = (i+kx, j+ky)
                        # 범위 | 락 < 키  좋아 | 락에 키 넣어야되는데 안했어 > 끝 | 락이 볼록, 키 볼록 > 끝
                        if (x >= 0 and y >= 0 and x < N and y < N):
                            if lock[x][y] == 0 and key[kx][ky] == 1:
                                cnt -= 1
                            if lock[x][y] == 0 and key[kx][ky] == 0:
                                keeptrying = False
                            if lock[x][y] == 1 and key[kx][ky] == 1:
                                keeptrying = False
                        if not keeptrying:
                            break
                    if not keeptrying:
                        break
                if cnt == 0:
                    ans = True
                if ans:
                    break
            if ans:
                break
        key = rotateCW(key)
    return ans
