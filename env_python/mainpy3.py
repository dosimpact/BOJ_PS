import re


def solution(line1, line2):
    answer = 0
    prints = []
    for i in range(0, len(line1)+1, 1):
        target = line1
        regLen = len(("&"*i).join(list(line2)))
        if (regLen > len(line1)):
            break
        # 정규식을 돌려볼 수 있으면 while문으로 돌려본다.
        regex = re.compile((i*"[a-z]").join(list(line2)))
        prints.append((regLen, regex, target))
        while regex.findall(target):
            res = regex.search(target)
            target = target[res.span()[0]+1:]
            answer += 1
    # print(prints)
    return answer
