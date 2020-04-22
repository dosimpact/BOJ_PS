


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000
    print(routes)
    answer = 0

    for route in routes:
        print(last_camera)
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]
    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
