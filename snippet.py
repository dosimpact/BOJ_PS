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


print(diver("()))((()"))
