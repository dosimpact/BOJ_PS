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


def isVaild(how: (), gidongs: [], bows: []):
    (x, y, a, b) = how  # a 기둥 , 보  | b 삭제 설치
    # 설치 | 기둥 |   # -기둥은 바닥위 | 기둥은 보의 한쪽끝 | 기둥은 기둥위
    if b == 1 and a == 0:

        pass
    elif b == 1 and a == 1:
        pass
    elif b == 0 and a == 0:
        pass
    elif b == 0 and a == 1:
        pass
    # 설치 | 보   # -보 조건 - 한쪽 끝 부분이 기둥위 | 양쪽끝이 보와 보 연결

    return False


def solution(n, build_frame):
    n = n+1
    gidongs = []
    bows = []
    # 빌드 프레임을 돌면서 하나씩 해보기
    for (x, y, a, b) in build_frame:  # 유효성 검사 후 -> 진행
        # 유효성 검사
        if isVaild((x, y, a, b), gidongs, bows):
            pass
        else:
            continue

        # 실행하기
