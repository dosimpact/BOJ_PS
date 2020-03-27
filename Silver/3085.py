import sys


def input(): return sys.stdin.readline().rstrip()


DEBUG = True

N = int(input())
graph = [list(input()) for _ in range(N)]


def maxVal():
    ans = 0
    # 잘못 생각? -> count로 단순히 그 행 또는 열의 수가 많은걸로 구함
    # fb 가장 긴 연속 부분(행 또는 열)을

    for i in range(N):
        tmp = 1
        for j in range(N-1):  # 0 1 2 3      [][][][][]
            if graph[i][j] == graph[i][j+1]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)

    for j in range(N):  # 0
        tmp = 1
        for i in range(N-1):  # 0 1 2 3
            if graph[i][j] == graph[i+1][j]:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        ans = max(ans, tmp)
    return ans


ansMax = 0
dx = [1, 0]
dy = [0, 1]
for i in range(N):
    for j in range(N):
        # fb) for k in range(4) : 구지 네 방향을 살필필요없어. 중복이 발생한다.
        for k in range(2):
            (nx, ny) = (i+dx[k], j+dy[k])
            if (nx >= 0 and ny >= 0 and nx < N and ny < N) and graph[i][j] != graph[nx][ny]:
                graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
                ansMax = max(ansMax, maxVal())
                graph[nx][ny], graph[i][j] = graph[i][j], graph[nx][ny]
print(ansMax)

"""
3
YZZ
ZYZ
ZZY
[['Y', 'C', 'P', 'Z', 'Y'], 
['C', 'Y', 'Z', 'Z', 'P'], 
['C', 'C', 'P', 'P', 'P'], 
['C', 'Y', 'Y', 'Z', 'C'], 
['C', 'P', 'P', 'Z', 'Z']]
"""
