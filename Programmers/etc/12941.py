

def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    res = 0
    for (i, j) in zip(A, B):
        res += i*j
    return res
