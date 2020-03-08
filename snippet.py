def solution(numbers):
    answer = ''
    res = list(map(str, numbers))
    import functools
    res = sorted(res, key=functools.cmp_to_key(
        lambda x, y: int(x+y) - int(y+x)), reverse=True)
    for r in res:
        answer += r
    # return answer
    return str(int(answer))


print(solution([0, 0, 0, 00]))
