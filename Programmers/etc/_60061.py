"""
https://programmers.co.kr/learn/courses/30/lessons/60061
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 합니다


벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,



"""

import sys
import copy

DEBUG = False


def isVaild(gidong: [], bow: []):
    if DEBUG:
        print(gidong)
        print(bow)
        print("-->vaild check start : ")
    # 유효성 검사하는 로직을 짜.
    # -기둥은 바닥위 | 기둥은 보의 한쪽끝 | 기둥은 기둥위
    for i in range(len(gidong)):
        x, y, _ = gidong[i]
        if y == 0:
            continue
        if y != 0:
            res = list(
                filter(lambda b: (b[0] == x-1 and b[1] == y) or (b[0] == x and b[1] == y), bow))
            if len(res) >= 1:
                continue
        if y != 0:
            res = list(filter(lambda g: g[0] == x and g[1] == y-1, gidong))
            if len(res) >= 1:
                continue
        return False
    # -보 조건 - 한쪽 끝 부분이 기둥위 | 양쪽끝이 보와 보 연결
    for i in range(len(bow)):
        x, y, _ = bow[i]
        res = list(
            filter(lambda g: (g[0] == x and g[1] == y-1) or (g[0] == x+1 and g[1] == y - 1), gidong))
        if len(res) >= 1:
            continue
        res = list(filter(lambda g:  (
            g[0] == x-1 and g[1] == y) or (g[0] == x+1 and g[1] == y), bow))
        if len(res) >= 2:
            continue
        if DEBUG:
            print("안 유효함 bow ❌", x, y)
        return False
    return True


def solution(n, build_frame):
    n = n+1
    gidongs = []
    bows = []

    # 빌드 프레임을 돌면서 하나씩 해보기
    for (x, y, a, b) in build_frame:  # 우선 그 작업을 해봐
        tmp_gidongs = copy.deepcopy(gidongs)
        tmp_bows = copy.deepcopy(bows)
        if DEBUG:
            print(x, y, a, b)
        if b == 0:  # 삭제
            if a == 0:  # 기둥
                gidongs = list(filter(lambda g: not (
                    g[0] == x and g[1] == y), gidongs))
            else:  # 보
                bows = list(filter(lambda b: not (
                    b[0] == x and b[1] == y), bows))
        elif b == 1:  # 생성
            if a == 0:  # 기둥
                gidongs.append([x, y, 0])
            else:  # 보
                bows.append([x, y, 1])
        print()
        if isVaild(gidongs, bows):
            if DEBUG:
                print("유요함 ✔-> ", gidongs, bows)
            continue
        else:
            gidongs = tmp_gidongs
            bows = tmp_bows
            if DEBUG:
                print("안 유요함 ❌ ->", gidongs, bows)

    # 유효성 통과시, 진행

    # 아니라면 버리기.

    # 최종 결과를 반환하는 로직
    fResult = gidongs+bows
    fResult.sort(key=lambda e: (e[0], e[1], e[2]))
    print(fResult)
    return fResult


solution(5,	[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [
         2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
