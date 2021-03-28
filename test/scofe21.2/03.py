from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline

DEBUG = True


class Node(object):
    def __init__(self, key, log=""):
        self.key = key  # 현재 나의 데이터
        self.log = set()  # 나를 스처간 자식들 ,str
        self.child = {}  # Node

    def __str__(self):
        return f"{self.key} | {self.log}"


class Trie(object):
    def __init__(self):
        self.head = Node("0")

    # a를 찾는다, 없다면 만들어 | 그리고 바로 아래 b를 달아
    def insert(self, a: str, b: str):
        cur_node = self.head
        # a가 트리에 없는경우 , 루드 아래 바로 만들어
        if a not in cur_node.log:
            cur_node.child[a] = Node(a)
            cur_node.log.add(a)
            cur_node.log.add(b)

            cur_node = cur_node.child[a]  # a로 교체
            if DEBUG:
                print(f"create {a}")
        elif a in cur_node.log:
            cur_node.log.add(b)
            while True:  # a도착할때까지
                if cur_node.key == a:
                    break
                if DEBUG:
                    print(f"cur_node.child {cur_node.child}")
                for nxt_node in cur_node.child.keys():  # 다음노드 탐색해봐
                    if a in nxt_node.log:  # 다음노드의 로그에도 있다면
                        nxt_node.log.add(b)
                        cur_node = nxt_node
                        break
                if DEBUG:
                    print("Error a log 모순")
        # a가 있는 경우, 자식을 들어가면서 a가 있는 쪽으로 간다. key가 a라면 중단
        # 붙여
        cur_node.child[b] = Node(b)  # a-b 연결
        cur_node.log.add(b)  # a에 b로그 남겨
        return

    # a까지 찾아 그리고 하위 요소들을 bfs로 모아
    def prefix(self, a: str):
        # a가 없는 경우 ->[]
        cur_node = self.head
        if a not in cur_node.log:
            return ""
        # a가 있는 경우, 자식을 들어가면서 key a가 나올때까지 순회
        if a in cur_node.log:
            print(f"cur_node {cur_node}")
            while True:
                if cur_node.key == a:
                    break
                print(f" cur_node {cur_node}")
                for nxt_node in cur_node.child.keys():
                    if a in nxt_node.log:
                        cur_node = nxt_node
        # key a가 가진 노도의 ->log 리턴
        return cur_node.log


mainTrie = Trie()
N, Q = map(int, input().split())
for _ in range(N):
    a, b = map(str, input().split())
    mainTrie.insert(a, b)
for _ in range(Q):
    a, b = map(str, input().split())
    qRes = mainTrie.prefix(a)
    print(qRes)  # b가 있는지 확인->Yes,No

"""
6 6

6 4  # 6이 상위다.
6 5
4 1
4 2
4 3
1 4

4 1 # 4가 상위냐 ?
6 5
1 6
6 3
4 3
"""


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
3 3
6 4
6 5
4 1
6 0
4 0
1 0
"""