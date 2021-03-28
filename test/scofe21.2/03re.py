from sys import stdin

input = stdin.readline

DEBUG = True


class Node(object):
    def __init__(self, key):
        self.key = key  # 현재 나의 데이터
        self.log = set()  # 나를 스처간 자식들 ,str
        self.child = {}  # Node
        self.log.add(key)

    def __str__(self):
        return f"{self.key} | {self.log}"


class Trie(object):
    def __init__(self):
        self.head = Node("0")
        self.memo = dict()

    # a를 넣고 마지막 노드 출력
    def insert(self, a: str, b: str):  # b는
        # a노드까지
        cur_node = self.head

        if a in cur_node.log:  # a가 있는 경우
            cur_node.log.add(b)
            while True:
                if cur_node.key == a:
                    break
                for nxt_node in cur_node.child.values():
                    if DEBUG:
                        print(f"nxt_node {nxt_node}")
                    if a in nxt_node.log:
                        nxt_node.log.add(b)
                        cur_node = nxt_node
        else:
            cur_node.child[a] = Node(a)
            cur_node.log.add(a)
            cur_node.log.add(b)
            cur_node = cur_node.child[a]

        if DEBUG:
            print(f"{a} node search complete {cur_node}")
        # a노드에서 b추가
        cur_node.child[b] = Node(b)
        cur_node.log.add(b)
        return

    def prefix(self, a: str):
        if a in self.memo:
            return self.memo[a]

        cur_node = self.head
        while True:
            if cur_node.key == a:
                break
            for nxt_node in cur_node.child.values():
                if a in nxt_node.log:
                    cur_node = nxt_node

        self.memo[a] = cur_node.log
        return cur_node.log


mainTrie = Trie()
N, Q = map(int, input().split())
for _ in range(N - 1):
    a, b = map(str, input().split())
    mainTrie.insert(a, b)
for _ in range(Q):
    a, b = map(str, input().split())
    qRes = mainTrie.prefix(a)
    if DEBUG:
        print(qRes)  # b가 있는지 확인->Yes,No
    if b in qRes:
        print("yes")
    else:
        print("no")


"""
6 6
6 4
6 5
4 1
4 2
4 3
1 4
4 1
6 5
1 6
6 3
4 3
"""

"""
4 3
6 4
6 5
4 1
6 0
4 0
1 0
"""