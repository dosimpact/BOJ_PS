import sys
from collections import deque
from copy import deepcopy


input = sys.stdin.readline

# 입력
N = int(input())
graph = [[] for _ in range(N)]
ansMax = 0
ansList = []

for _ in range(N * 3):
    row = map(int, input().split(" "))
    for idx, e in enumerate(row):
        graph[idx].append(e)
for row in graph:
    row.reverse()


def printG(cgraph):
    for g in cgraph:
        print(*g)


# 점수 = 사라진 차 갯수
# + 차고칸 포함 가장 작은 직사각형

# 아래로 떨어저 빈칸 채운다. 계속 떨어진다.
# 3차례 반복 -> 가장 큰 점수

# 열을 떨구는 기능

# 현재 차고에서 가장 많이 있는


def BFS(graph, check, sx, sy, checkCount):
    # 주어진 그래프에서 BFS를 수행하여
    q = deque()
    check[sx][sy] = checkCount
    q.append((sx, sy))
    pointCount = 1
    pointList = [(sx, sy)]
    # 요소들의 좌표를 수집
    while q:
        x, y = q.popleft()
        # 주변을 탐색한다. | 방문여부 | 범위 | (방문가능-차의 색깔)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if check[nx][ny] != 0:
                continue
            if graph[x][y] != graph[nx][ny]:
                continue
            check[nx][ny] = check[x][y]
            pointList.append((nx, ny))
            q.append((nx, ny))
            pointCount += 1
    # 요소의 수와, width,heigh를 곱해 점수, 좌표셋 리턴
    xlist = [e[0] for e in pointList]
    ylist = [e[1] for e in pointList]
    xSpan = abs(min(xlist) - max(xlist)) + 1
    ySpan = abs(min(ylist) - max(ylist)) + 1
    # 같은 차 색깔과, 직사각형
    score = pointCount + xSpan * ySpan
    return (score, pointList)


def removeCars(copiedGraph, comPoints):
    for x, y in comPoints:
        copiedGraph[x][y] = 0
    return


def fillCars(copiedGraph):
    for i in range(len(copiedGraph)):
        data = copiedGraph[i]
        N = len(data)
        data = list(map(str, data))
        res = list(map(int, list("".join(data).replace("0", "").ljust(N, "0"))))
        copiedGraph[i] = res


def go(score, graph, count, scoreLog):
    global ansMax
    if count == 3:
        ansMax = max(ansMax, score)
        # ansList.append(score)
        # print("fin : scoreLog", scoreLog)
        return
    # 컴포넌트 분리되어 , 각 점수(갯수+가장큰직)
    check = [[0 for _ in range(N)] for _ in range(N)]
    checkCount = 1
    comStateList = []
    # 재귀함수의 state 중 check 이다.
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                result = BFS(graph, check, i, j, checkCount)
                comStateList.append(result)
    # 컴포넌트의 상태 리스트 구하기
    comStateList.sort(key=lambda x: (x[0]), reverse=True)
    # print(comStateList)
    # exit(0)
    for comScore, comPoints in comStateList:
        copiedGraph = deepcopy(graph)
        # 좌표의 차들 제거
        removeCars(copiedGraph, comPoints)
        # 좌표의 차들 채우기
        fillCars(copiedGraph)
        # nextgo호출
        go(score + comScore, copiedGraph, count + 1, scoreLog + [comScore])
        # exit(0)


go(0, graph, 0, [])
print(ansMax)
# print(ansList)
"""
2
1 1
2 2
1 1
3 3
4 4
1 2

2
1 1
2 2
1 1
3 3
4 4
4 2


2
1 1
1 1
1 1
1 1
1 1
1 1

2
1 6
1 5
1 4
1 3
1 2
1 1

2
1 6
1 5
1 4
1 3
1 2
1 7

15
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1


"""
