
import sys


def input(): return sys.stdin.readline().rstrip()


def solution(skills, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        can = True
        qqu = list(skills)
        for skill in skill_tree:
            if skill in qqu:
                if qqu.index(skill) != 0:
                    can = False
                    break
                else:
                    qqu.pop(0)
        if can:
            answer += 1
    return answer


solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"])
