import sys


MAX_VAL = 9
# d의
d = [set() for _ in range(MAX_VAL)]


def interEval(a: set, b: set):
    res = set()
    for k in range(4):
        for ae in a:
            for be in b:
                if k == 0:
                    res.add(ae+be)
                if k == 1:
                    res.add(ae-be)
                if k == 2:
                    res.add(ae*be)
                if k == 3 and be != 0:
                    res.add(ae//be)
    return res


def solution(N, number):
    # init d
    for i in range(1, MAX_VAL):
        d[i] = d[i] | {int(f"{N}"*i)}

    for i in range(2, MAX_VAL):  # 3
        for j in range(1, i):
            d[i] = d[i] | (interEval(d[j], d[i-j]))
    for i in range(1, MAX_VAL):
        if number in d[i]:
            return i
    return -1


print(solution(5, 12))
