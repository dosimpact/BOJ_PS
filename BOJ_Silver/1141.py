import sys
sys.setrecursionlimit(10**6)


def input(): return sys.stdin.readline().rstrip()

"""
단어 열 탐색
접두 관계가 있으면
작은 녀석이 패배(길이)
"""

ans = []

N = int(input())
sen = []
for i in range(N):
    sen.append(input())

for e in sen:
    isposs = True
    why = ""
    for an in ans:
        if an.startswith(e) or e.startswith(an):
            isposs = False
            why = an
    if isposs:  # 가능한경우 그냥 넣어
        ans.append(e)
        pass
    else:
        # 불가능한 경우, 짧은단어를 골라서 교체
        if(len(why) >= len(e)):
            pass
        else:
            idx = ans.index(why)
            ans.pop(idx)
            ans.append(e)
print(len(ans))
