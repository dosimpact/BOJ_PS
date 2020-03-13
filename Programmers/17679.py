"""
https://programmers.co.kr/learn/courses/30/lessons/17679

시뮬레이션 및 구현 문제

#1. 보드를 90 도 회전시킨다.


# 전체 board를 돌면서 2*2 블럭을 보이면 지울거라는 mark를 새긴다.

board_mark에 체크 1로

# board에 빈공간은 x로 만들며

# replace로 처리

"""


def solution(m, n, board):
    answer = 0
    graph = [['0' for _ in range(m)] for _ in range(n)]
    for i in range(n):  # 5 세로
        for j in range(m):
            graph[i][j] = board[m-1-j][i]
    # print(graph)
    # n , m 으로 접근하면 됨 5  ,4
    while True:
        #print('-->1', graph)
        isgo = False
        gc = [[0 for _ in range(m)] for _ in range(n)]
        # 지울수 있는것들 체크
        for i in range(n):
            for j in range(m):
                if i+1 < n and j+1 < m:
                    if graph[i][j] != '.' and graph[i][j] == graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1]:
                        gc[i][j] = gc[i][j + 1] = gc[i+1][j] = gc[i+1][j+1] = 1
                        isgo = True
        #print('-->2', graph)
        #print('-->2', gc)
        if not isgo:
            break
        # 지우기
        for i in range(n):
            for j in range(m):
                if gc[i][j] == 1:
                    graph[i][j] = '.'
        # 밀기
        #print('-->3', graph)
        for i, rowArr in enumerate(graph):
            rowStr = "".join(rowArr)
            rowStr = "".join(list(filter(lambda e: e != '.', rowStr)))
            rowStr = rowStr.ljust(m, '.')
            graph[i] = list(rowStr)
        #print('-->4', graph)
    for grow in graph:
        answer += grow.count('.')
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(2, 2, ["AA", "AA"]))

"""
fb1.
배열 다시 파싱하는거 너무 어렵다.
중력의 작용하는 방향의 시작점이 0이 되어야한다.
처음에 반대로 했다가 게임이 바뀌어 버렸어.

fb2. 아니, 프렌트 케릭터의 앞글자만 문자로 주어지는줄 알았더니만,
A-Z 까지 전부 주어진다네 ;;;;;;
빈 공간을 'X'로 표현했다가 털림
"""
