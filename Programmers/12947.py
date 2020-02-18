def solution(x):
    answer = True
    xlist = list(str(x))
    sum = 0
    for e in xlist:
        sum += int(e)
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer
    sum()
