

import sys


def input(): return sys.stdin.readline().rstrip()


"""

5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT

5 8
CATGATAC
AAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
"""

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

# print(data)

ansDNA = []
ansDNADis = 0

for idx, col in enumerate(zip(*data)):
    ATGC = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
    }
    for e in col:
        ATGC[e] += 1
    Maxres = max(ATGC.values())
    ansDNADis += N - Maxres
    for key in ATGC:
        #print(f"{idx} => {key}")
        if ATGC[key] == Maxres:
            print(key, end="")
            break
print()
print(ansDNADis)
