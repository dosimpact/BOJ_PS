
import sys
from collections import deque


<<<<<<< HEAD
    def insert(self, string):
        nnode = self.head
        # 해당 string을 돌면서, 해당 문자열이 나올때까지, 계속 추가하기
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
        nnode.data = string

    def search(self, string):
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return False
        if nnode.data != None:
            return True

    def starts_with(self, prefix):
        nnode = self.head
        result = []
        subtrie = None
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
                subtrie = nnode
            else:
                return result
        q = list(subtrie.children.values())

        while q:
            now = q.pop()
            if now.data != None:
                result.append(now.data)
            q += list(now.children.values())
        return result


Ma = Trie()
Ma.insert("cross")
Ma.insert("crocus")
Ma.insert("crossHex")
print(Ma.search("corss"))  # False
print(Ma.search("cross"))  # True
print(Ma.starts_with("cro"))  # ['crocus', 'cross', 'crossHex']
print(Ma.starts_with("cross"))  # ['crossHex']
print(Ma.starts_with("t")) #[]
=======
def input(): return sys.stdin.readline().rstrip()


"""
나이트의 이동

8 한변의 길이
00 나이트의 현재칸
70 목표 칸
"""

# bfs 탐색


t = int(input())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(t):
    L = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    check = [[-1 for _ in range(L)] for _ in range(L)]
    dq = deque()
    dq.append((sx, sy))
    check[sx][sy] = 0
    isEnd = False

    if sx == gx and sy == gy:
        print(0)
        continue

    while len(dq) > 0:
        x, y = dq.popleft()

        for k in range(len(dx)):
            nx, ny = x+dx[k], y+dy[k]
            if (nx >= 0 and ny >= 0 and nx < L and ny < L) and (check[nx][ny] == -1):
                check[nx][ny] = check[x][y] + 1
                dq.append((nx, ny))
                if nx == gx and ny == gy:
                    print(check[nx][ny])
                    isEnd = True
                    break
        if isEnd:
            break

"""
1
8
0 0
7 0
"""

arr = []
# 앞에서 넣고 뺴고
arr.pop(0)
arr.insert(0, 1)

# 뒤에서 넣고 빼고
arr.pop()
arr.append(1)

dq = deque()

# 앞에서 넣고 뺴고
dq.appendleft(1)
dq.popleft()

# 뒤에서 넣고 빼고
dq.append(1)
dq.pop()


"""
fb)


"""
>>>>>>> 6c9bce59587d3102dfdb55c0cf825cfb0ecfc81c
