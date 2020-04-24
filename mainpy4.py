

import sys


def input(): return sys.stdin.readline().rstrip()


"""
각 원소의 합이 S가 되는 수의 집합
위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
"""

#


def solution(n, works: []):  # 5 | 4 3 2 1
    works.sort(reverse=True)

    for i in range(len(works)-1):
        diff = abs(works[i]-works[i+1])
        if diff == 0:
            continue
        if n - diff*(i+1) >= 0:
            for j in range(0, i+1):
                works[j] -= diff
            n -= diff*(i+1)
        else:
            for j in range(0, n):
                works[j] -= 1
            break
    print(n)  # 8, [3,3,3]

    if n >= sum(works):
        return 0
    u, v = divmod(n, len(works))
    for idx in range(len(works)):
        works[idx] -= u
    for idx in range(v):
        works[idx] -= 1

    print(works)
    ans = 0
    for work in works:
        ans += work**2
    return ans


print(solution(1, [2, 1, 2]))
# print(solution(4, [7, 5, 4, 4, 3, 2]))
# print(solution(3, [1, 1, 1]))
# print(solution(4, [1, 1, 1]))
# print(solution(1, [1, 2, 2]))
# print(solution(1, [1, 2, 3, 4]))
"""
def solution(n, works: []):  # 무조건 최고의 workㄹ르 줄여라
    answer = 0

    for _ in range(n):
        idx = works.index(max(works))
        if(works[idx] > 0):
            works[idx] -= 1
        else:
            break
    print(works)
    for work in works:
        answer += work**2
    return answer

print(solution(3, [1, 1]))
"""


"""
def solution(n, works: []):
    WLen = len(works)  # 5 4 3 2 1 , 7
    res = sum(works) - n  # 15 - 7 = 8
    if res <= 0:
        return 0
    u, v = divmod(res, WLen)  # 1 3 >  2 2 2 1 1
    ans = [u]*WLen
    for idx in range(v):
        ans[idx] += 1
    fans = 0
    print(ans)
    for an in ans:
        fans += an**2
    return fans
"""
