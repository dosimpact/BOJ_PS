
import sys


input = sys.stdin.readline

goalState = "123456780"
state = ""
check = dict()
for _ in range(3):
    state += "".join(input().split())
# state = state.replace("0", "9")
# print(state)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = [state]
check[state] = 0
while q:
    now = q.pop(0)  # 103425786
    zeroIdx = now.find('0')
    x, y = zeroIdx // 3, zeroIdx % 3
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or ny < 0 or nx >= 3 or ny >= 3:
            continue

        next = list(now)
        tmp = next[zeroIdx]
        next[zeroIdx] = next[nx*3+ny]
        next[nx*3+ny] = tmp
        next = "".join(next)

        if next in check:
            continue
        check[next] = check[now] + 1
        if next == goalState:
            break
        q.append(next)

if goalState in check:
    print(check[goalState])
else:
    print(-1)
"""
103
425
786


"""
