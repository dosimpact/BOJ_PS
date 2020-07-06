import sys


def input(): return sys.stdin.readline().rstrip()


GGu = "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
noyGGu = "흥칫뿡!! <(￣ ﹌ ￣)>"

su = input()

if len(su) == 1:
    print(GGu)
    exit(0)

inter = int(su[0]) - int(su[1])

for i in range(1, len(su)-1):  # i와 i+1를 비교
    if inter != (int(su[i]) - int(su[i+1])):
        print(noyGGu)
        exit(0)
print(GGu)
