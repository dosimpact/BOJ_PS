from sys import setrecursionlimit, stdin
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 8)

# 트라이 자료구조
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string: str):
        now = self.head
        for s in string:
            if s not in now.child:
                now.child[s] = Node(s)
            now = now.child[s]
        now.data = string

    def search(self, prefix: str):  # prefix 와 같은 길이 문자열은 처음에 박힌다.
        now = self.head
        for p in prefix:
            if p not in now.child:
                return False
            now = now.child[p]
        if now.data:
            return True
        else:
            return False

    def start_with(self, prefix: str):  # prefix 와 같은 길이 문자열은 처음에 박힌다.
        now = self.head
        for p in prefix:
            if p not in now.child:
                return []
            now = now.child[p]
        ans = []
        dq = deque()
        if now.data:
            ans.append(now.data)
        dq.extend(now.child.values())
        while dq:
            now = dq.popleft()
            if now.data:
                ans.append(now.data)
            dq.extend(now.child.values())
        return ans


mainTrie = Trie()
# 재귀함수 작성하기
W = int(input())
for _ in range(W):
    word = input().strip()
    mainTrie.insert(word)
input()
# 단어 점수, 가장긴 단어, 찾은 갯수
ansData = set()
board = []


def go(x: int, y: int, prefix: str, check, node):
    if node.data:
        ansData.add(node.data)
    # searchs = mainTrie.start_with(prefix)
    # if len(searchs) == 0:
    # return
    # while len(searchs) >= 1 and len(searchs[0]) == len(prefix):
    # ansData.append(searchs[0])
    # searchs = searchs[1:]
    # if len(searchs) >= 1:
    for dx, dy in zip([0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, -1, 1, -1, 1]):
        nx, ny = x + dx, y + dy
        if not (nx >= 0 and ny >= 0 and nx < 4 and ny < 4):
            continue
        if check[nx][ny]:
            continue
        if board[nx][ny] in node.child.keys():
            check[nx][ny] = True
            go(nx, ny, prefix + board[nx][ny], check, node.child[board[nx][ny]])
            check[nx][ny] = False


score = [0, 0, 0, 1, 1, 2, 3, 5, 11, 0, 0]
B = int(input())
for b in range(B):
    board = []
    check = [[False for _ in range(4)] for _ in range(4)]
    for _ in range(4):
        board.append(input().strip())
    if b != B - 1:
        input()
    for i in range(4):
        for j in range(4):
            if board[i][j] in mainTrie.head.child.keys():
                check[i][j] = True
                go(i, j, board[i][j], check, mainTrie.head.child[board[i][j]])
                check[i][j] = False
    ansData = list(ansData)
    ansData.sort(key=lambda x: (-len(x), x))
    if len(ansData) == 0:
        ansData = set()
        continue
    a, b, c = 0, ansData[0], len(ansData)
    for d in ansData:
        a += score[len(d)]
    print(a, b, c)
    ansData = set()

"""
✅ 시간 계선 
- 보글판 돌면서 매번 start_with X
- 매번 하위 요소들까지 검색할 필요 있나 ?
- start_with가 아닌 search만 봐도 된다.
- 하위 자식의 수를 저장하는 값 추가
- prefix를 타고 가는것이 아닌 Tree의 노드를 타고 간다면 ? 

- DFS를 이용한다.
- 보글에서 8방향을 순회한다.
- 8방향에서, 다음으로 가고 싶은데, Trie에서도 다음(자식)이 있으면 간다.
"""

"""
✅ 중복칸 제거
2
ABA 
AB

1
ABCD
EFGH
IJKL
MNOP
"""

"""
✅ 사전순 체크
3
CCCC
AAAA
BBBB

1
AAAA
BBBB
CCCC
DDDD
"""

"""
점수 체크
10
A
AB
ABA
ABAB    
ABABABAB
Z
ZX
ZXZ
ZXZX
ABABABAZ

1
AAAA
BBBB
CCCC
DDDD
"""

"""
✅ 대각선 순회
5
N
NEST
NESTIAA
NZßSTIAAC
NESTIAAZ

1
ACMA
APCA
TOGI
NEST
"""
"""
5
ICPC
ACM
CONTEST
GCPC
PROGRAMM

3
ACMA
APCA
TOGI
NEST

PCMM
RXAI
ORCN
GPCG

ICPC
GCPC
ICPC
GCPC
"""
"""
testTrie = Trie()
testTrie.insert("hello")
testTrie.insert("hell")
testTrie.insert("heaven")
print(testTrie.start_with("h"))
print(testTrie.start_with("he"))
print(testTrie.start_with("hell"))
print(testTrie.start_with("hello"))
"""
