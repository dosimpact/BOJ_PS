

import sys

Debug = False


def input(): return sys.stdin.readline().rstrip()


"""
12 2 // 고객을 12명 늘리고 싶다. 2개 정보가 이싸
3 5 // 3원을 사용해서 고객 5명 늘릴 수 있다.
1 1
"""

# 돈의 최솟값

C, N = map(int, input().split())
data = []
for _ in range(N):
    u, v = map(int, input().split())
    data.append((u, v))

# print(data)


data.sort(key=lambda e: (e[1]/e[0], e[0]), reverse=True)
metaData = list(map(lambda e: (e[1]/e[0]), data))
# print(data)
# print(metaData)


pleft = C  # C명남음
ansMony = 0
MonyList = []

for i in range(len(data)):
    # 채워
    u, v = divmod(pleft, data[i][1])
    ansMony += u*data[i][0]
    MonyList.append(ansMony + data[i][0])
    pleft = v
    if pleft <= 0:  # 중간에 다채우면 종료
        break

# 끝까지 온경우는 | 최적으로 C명을 되는데까지 채움.

if pleft != 0:  # 문제의 상황 ,모든 경우들이 커버를 한번씩 해보며 최소머니를 찾는다.
    print(min(MonyList))
else:
    print(ansMony)


# 원당 고객확보가 같다면, 우선순위는 , 원수가 작은거에 있다.


"""
12 2
3 5
1 1

45 2
7 17
4 9

"""
