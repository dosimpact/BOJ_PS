import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None) -> None:
        super().__init__()
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self) -> None:
        super().__init__()
        self.head = Node(None)

    def insert(self, string: str):
        cur_node = self.head
        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)
            cur_node = cur_node.children[s]
        cur_node.data = string
        # print("DEBUG ", string, " inserted")

    # True,False
    def startsWith(self, string: str):
        # 접두사 까지 탐색을 시도
        cur_node = self.head
        for s in string:
            if s in cur_node.children:
                cur_node = cur_node.children[s]
            else:
                return False
        # 접두사 이후
        if cur_node.children:
            return True
        else:
            return False


def sol(wordList):
    trie = Trie()
    for w in wordList:
        trie.insert(w)
    for w in wordList:
        res = trie.startsWith(w)
        # print(f" w {w} res {res}")
        if res == True:
            print("NO")
            return
    print("YES")


N = int(input())
for i in range(N):
    wordsu = int(input().strip())
    wordList = []
    for _ in range(wordsu):
        wordList.append(input().strip())
    sol(wordList)

# trie = Trie()
# for s in ["911", "97625999", "91125426"]:
#     trie.insert(s)
# for s in ["911", "97625999", "91125426"]:
#     print(trie.startsWith(s))

"""
t = 50
n = 10**4 (갯수)
L = 10 (길이)
>입력 : n*L = 10**5
>출력 : n*L = 10**5
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
"""
