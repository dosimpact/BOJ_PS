
# https://www.acmicpc.net/problem/3101
import sys


def input(): return sys.stdin.readline().rstrip()


N, K = map(int, input().split())  # N 메타데이터 -> 크기가 N자리
cmd = list(input())

SIZE = N*2 - 1  # 11
Meta = []


now = 1

for i in range(1, (SIZE//2)+2, 1):  # 1,2,3,(4) #현재 now를 meta에 넣고 |
    Meta.append([now])
    now += i
for i in range(SIZE//2, 0, -1):  # 3,2,1
    Meta.append([now])
    now += i


def graph(i, j):
    if((i+j) % 2) == 1:
        if (i+j) <= (SIZE//2):
            return (Meta[i+j][0] + i)
        else:
            return (Meta[i+j][0] + (i - (i+j - SIZE//2)))
    else:
        if (i+j) <= SIZE//2:
            return (Meta[i+j][0] + j)
        else:
            return (Meta[i+j][0] + (j - (i+j - SIZE//2)))


nowPosition = (0, 0)
ans = 0
ans += graph(nowPosition[0], nowPosition[1])
for c in cmd:  # 이동하고 범위는 체크를 안한다 -> 값만 더해준다.
    i, j = nowPosition
    if c == 'D':
        nowPosition = (i+1, j)
        ans += graph(nowPosition[0], nowPosition[1])
    elif c == 'R':
        nowPosition = (i, j+1)
        ans += graph(nowPosition[0], nowPosition[1])
    elif c == 'U':
        nowPosition = (i-1, j)
        ans += graph(nowPosition[0], nowPosition[1])
    else:  # L
        nowPosition = (i, j-1)
        ans += graph(nowPosition[0], nowPosition[1])
print(ans)
