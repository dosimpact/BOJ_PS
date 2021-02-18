
def isBal(s: str):
    return s.count("(") == s.count(")")


def isCor(s: str):
    cnt = 0
    for se in s:
        if se == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt > 0:
        return False
    else:
        return True


def diver(s: str):
    cnt = 0
    idx = 0
    for i, se in enumerate(s):
        if se == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return (s[:i+1], s[i+1:])
    return "ERROR"


def dirRever(s: str):
    res = []
    for se in list(s):
        if se == "(":
            res.append(')')
        else:
            res.append('(')
    return "".join(res)


def go(s: str):
    # baseCase
    if s == "":
        return s
    u, v = diver(s)
    if isCor(u):
        return u + go(v)
    else:
        return f'({go(v)})' + dirRever(u[1:-1])


def solution(p):
    if isCor(p):
        return p
    answer = go(p)
    return answer


print(solution(")))()((("))
