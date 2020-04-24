
import heapq


def solution(n, works: []):  # 무조건 최고의 workㄹ르 줄여라
    answer = 0
    newWorks = list(map(lambda e: -e, works))
    heapq.heapify(newWorks)
    print(newWorks)

    for _ in range(n):

        if newWorks[0] == 0:
            return 0
        else:
            w = heapq.heappop(newWorks)
            heapq.heappush(newWorks, w+1)

    # print(works)
    for work in newWorks:
        answer += abs(work)**2
    return answer


print(solution(4, [4, 3, 3]	))
print(solution(3, [1, 1]))
