import sys
import math
import re
import heapq
from collections import deque
from typing import *
import copy
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

# 아이디 길이, 3~15자 이하, 알파 소무낮, 숫자 ,-,_,.
# . 처음 끝 사용 불가, 연속 사용 불가


def isOk(x: str):
    return x.isalnum() or x in ["-", "_", "."]


def solution(new_id: str):
    new_id = new_id.lower()
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = "".join(list(filter(isOk, new_id)))
    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while ".." in new_id:
        p = new_id.find("..")
        new_id = new_id[:p]+new_id[p+1:]
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = "a"
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if new_id and new_id[-1] == ".":
            new_id = new_id[:-1]
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) <= 2:
        new_id = new_id+new_id[-1]
    return new_id
