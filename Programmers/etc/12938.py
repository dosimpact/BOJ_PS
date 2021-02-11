def solution(n, s):  # 3,10 > 3 3 4 # 3,11 > 3 4 4
    mins = sum([1 for i in range(1, n+1)])
    if s < mins:
        return [-1]
    u, v = divmod(s, n)
    ans = [u]*n
    for rest in range(v):
        ans[rest] += 1
    ans.sort()
    return ans


print(solution(2, 2))
