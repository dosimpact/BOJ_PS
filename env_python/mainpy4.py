import sys


def input(): return sys.stdin.readline().rstrip()


# https://www.acmicpc.net/problem/9328


T = int(input())
graph = []
keys = []
X, Y = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
sub_q = []


def inRange(x, y):
    return x >= 0 and y >= 0 and x < X+2 and y < Y+2


for _ in range(T):
    X, Y = map(int, input().split())
    # =========== init ===========
    graph = [["."] + list(input()) + ["."] for _ in range(X)]
    graph.insert(0, ["." for _ in range(Y+2)])
    graph.append(["." for _ in range(Y+2)])
    check = [[0 for _ in range(Y+2)] for _ in range(X+2)]
    keys = [0 for _ in range(ord('a'), ord('z')+1)]
    # for key in range(ord('A'), ord('Z')+1):
    # sub_q[chr(key)-'A'] = []
    sub_q = [[] for _ in range(ord('A'), ord('Z')+1)]
    keys_tmp = list(input())
    for k in keys_tmp:
        if k == "0":
            continue
        keys[ord(k)-ord('a')] += 1
    isKeyChange = True

    # 0,0 부터 BFS 로 탐색을 한다.
    check[0][0] = 0
    q = [(0, 0)]
    ans = 0
    while q:
        x, y = q.pop(0)
        # 서브 큐 추가
        if isKeyChange:
            for i in range(0, ord('z')-ord('a')+1):
                if len(sub_q[i]) != 0 and keys[i] == 1:
                    # q += [ sub_q[]]
                    while sub_q[i]:
                        q += [sub_q.pop(0)]
            isKeyChange = False

        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if not inRange(nx, ny) or check[nx][ny] != 0 or graph[nx][ny] == "*":
                continue
            # 다음이 벽인경우, 빈공간인 경우, 문서이 경우
            if graph[nx][ny] == ".":
                check[nx][ny] = 1
                q += [(nx, ny)]
            if graph[nx][ny] == "$":
                check[nx][ny] = 1
                q += [(nx, ny)]
                ans += 1
            # 문인 경우 - 열쇠가 있어, 없어
            if graph[nx][ny].isupper():
                check[nx][ny] = 1
                if keys[ord(graph[nx][ny]) - ord('a')] == 1:
                    q += [(nx, ny)]
                else:
                    sub_q[chr(graph[nx][ny])] += [(nx, ny)]
                # sub_q[graph[nx][ny]] += [(nx, ny)]
                # isKeyChange = True
            # 열쇠인 경우
            if graph[nx][ny].islower():
                check[nx][ny] = 1
                q += [(nx, ny)]
                keys[ord(graph[nx][ny])-'a'] = 1
                # keys += [graph[nx][ny]]
                isKeyChange = True
                # sub_q[graph[nx][ny]] += [(nx, ny)]
    print(ans)

# key가 추가되면 , 서브 큐 탐색
# key가 있으면
