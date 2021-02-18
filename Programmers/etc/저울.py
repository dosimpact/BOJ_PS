def solution(weight):
    weight.sort()
    if weight[0] != 1:
        return 1
    S, E = 1, 1
    print(weight)
    for i in range(1, len(weight)):
        NS, NE = weight[i], weight[i]+E  # 1,2
        print(f" {S},{E} + {NS},{NE} ", end="")
        # if E < NS:
        #     return E+1
        if E + 1 < NS:
            return E+1
        else:
            print(f"res {S},{NE} ")
            E = NE
    return E+1


print(solution([3, 1, 6, 2, 7, 20, 1]))

print(solution([1, 1, 3]))

"""
로직은 좋았으나, 
        # if E < NS:
        #     return E+1

이 부분에서 문제가 생겼다.
"""
