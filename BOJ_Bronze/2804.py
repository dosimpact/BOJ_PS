
import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


a, b = input().split()

res = list(set(a) & set(b))
idxList = [a.index(r) for r in res]


idxa = min(idxList)
dchar = a[idxa]
idxb = b.index(dchar)
if Debug:
    print(f"didx {idxa} dcahr {dchar} idxb { idxb}")

for i in range(len(b)):
    for j in range(len(a)):
        if i == idxb:
            print(a[j], end="")
        elif j == idxa:
            print(b[i], end="")
        else:
            print(".", end="")
    print()
