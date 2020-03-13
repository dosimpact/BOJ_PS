import functools
arr = [[3, 3], [3, 4], [3, 2], [2, 1], [4, 1]]


def cmp(x, y):
    if x[0] == y[0]:
        return x[1] - y[1]  # 1 2 #두번째는 오름차
    else:
        return y[0] - x[0]  # 첫번째는 내림차


print(arr)
arr.sort(key=functools.cmp_to_key(cmp))
print(arr)
