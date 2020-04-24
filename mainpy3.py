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
