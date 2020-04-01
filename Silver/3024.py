import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

graph = [list(input()) for _ in range(N)]


# XX..A..CCC...BBB


def isVaild(s: []):
    cnt = 0
    now = "."
    # .인경우는 무조건 초기화
    for i in range(len(s)):
        # .이 아닌 경우, 같은거 또 나온겨우
        if s[i] == '.':
            cnt = 0
            now = '.'
        else:
            if now == s[i]:
                cnt += 1
                if cnt >= 3:
                    return now
            else:
                now = s[i]
                cnt = 1

                # 다른게 나온경우. ( . 에서 새롭게 나온경우)
    return '.'


# 가로 탐색
for i in range(N):
    tmp = isVaild(graph[i])
    if(tmp != '.'):
        print(tmp)
        exit(0)

# 세로 탐색
for j in range(N):
    rcd = [graph[i][j] for i in range(N)]
    tmp = isVaild(rcd)
    if(tmp != '.'):
        print(tmp)
        exit(0)

# 대각선 오아 탬색
for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:
            rcd = [graph[i+k][j+k]
                   for k in range(N) if (i+k) < N and (j+k) < N]
            tmp = isVaild(rcd)
            if(tmp != '.'):
                print(tmp)
                exit(0)

# 대각선 왼아 탐색
for i in range(N):
    for j in range(N):
        if i == 0 or j == N-1:
            rcd = [graph[i+k][j-k]
                   for k in range(N) if (i+k) < N and 0 <= (j-k)]
            tmp = isVaild(rcd)
            if(tmp != '.'):
                print(tmp)
                exit(0)

print("ongoing")
"""
3
XXT
XTC
T..
"""
