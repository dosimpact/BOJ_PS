

import sys


def input(): return sys.stdin.readline().rstrip()


HTML = sys.stdin.read()

parsedHTML = ""
prevBlank = False
pointer = 0


def moveEndBlank(p: int):
    res = ' '
    while True:
        t = HTML[p+1]
        if t == '\n' or t == ' ':
            p += 1
        else:
            return (p, res)
    return -1


def processTag(p: int):
    res = ""
    HTMLType = HTML[p+1:p+3]
    if HTMLType == "br":
        res = "\n"
        return (p+3, res)
    elif HTMLType == "hr":
        res = "\n--------------------------------------------------------------------------------\n"
        return (p+3, res)
    return (-1, "ERROR")


while pointer < len(HTML)-1:
    t = ascii(HTML[pointer])
    #print(f"Debug: {t}")
    if t == ascii('\n') or t == ascii(' '):
        pointer, res = moveEndBlank(pointer)
        #print(f"Debug:moveEndBlank {pointer}")
        parsedHTML += res
    elif t == ascii('<'):
        tmpP, res = processTag(pointer)
        pointer = tmpP
        parsedHTML += res
    else:
        parsedHTML += HTML[pointer]
    pointer += 1
print(parsedHTML)

"""
a<br><br>c

1. <br> 다음의 공백도 처리

2. <hr> 앞뒤 공백 처리

2. 80글자 단위 출력


"""
