
import sys
from itertools import permutations
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


"""
L R 
8808 8880
[L R]
8808 3
8809 2
"""

L, R = map(int, input().split())

# 큰자리수를 기준으로 돌리면 됨.
MAXLEN = max(len(str(L)), len(str(R)))
AnsMin = min(str(L).count("8"), str(R).count("8"))

IList = [0]*11
Data = ["7", "8", "9"]


def go(idx: int):
    global AnsMin
    if idx == MAXLEN:
        Tmp = [Data[k] for k in IList[:MAXLEN]]
        res = "".join(Tmp)
        resInt = int(res)

        if L <= resInt and resInt <= R:
            print(f"{res} -> {resInt} : {res.count('8')}")
            AnsMin = min(AnsMin, res.count('8'))
        return
    for i in range(0, 3):
        IList[idx] = i
        go(idx+1)


if AnsMin == 0 or len(str(L)) != len(str(R)):
    print(0)
    exit(0)
else:
    Lt = list(str(L))
    Rt = list(str(R))
    j = 0
    for k in range(0, min(len(Lt), len(Rt))):
        if Lt[k] == Rt[k]:
            j += 1
        else:
            break
    Lt, Rt = Lt[j:], Rt[j:]
    print(Lt, Rt)
    MAXLEN = max(len(str(L)), len(str(R)))
    # go(0)

print(AnsMin)
