
# 양의 정수 n , k 진수로 바꿀때
check = None


def primeFilter(M):
    global check
    check = [0 for _ in range(M+1)]
    for i in range(2, M):
        if i**2 > M:
            break
        if check[i] == 0:
            for j in range(i*2, M+1, i):
                check[j] = 1


def converTo(src, q):
    result = ''
    while src > 0:
        src, mod = divmod(src, q)
        result += str(mod)
    return result[::-1]


def solution(n, k):
    ans = 0
    result = converTo(n, k)
    candiList = result.split("0")
    candiList = list(map(int, filter(lambda x: x, candiList)))
    maxVal = max(candiList)
    primeFilter(maxVal)
    # print(check)
    for c in candiList:
        if c == 1:
            continue
        if check[c] == 0:
            ans += 1
    return ans


# 	실패 (시간 초과)
print(solution(11001100, 10))
# print(solution(1111110111110111	, 10))


"""
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (0.25ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.5MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.05ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.5MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.04ms, 10.4MB)
"""
