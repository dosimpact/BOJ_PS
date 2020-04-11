"""
-R-A-M-

# 자주쓰는 알고리즘

-트라이 자료구조 구현하기 ✔
-행렬 회전하기 시계방향 90됴 ( 노말버전, 파이썬 버전 ) ✔
-다음 순열 구현하기 ✔
-gcd,LG 구현하기 ✔
-비트마스크로 모든 집합 순회하기 (1182 BOJ) ✔
"""

from collections import defaultdict


class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
        self.lengths = defaultdict(int)


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        # string 를 한바퀴 돌면서, node를 계속 연결해 준다.
        nnode = self.head
        nnode.lengths[len(string)] += 1
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
            nnode.lengths[len(string)] += 1
        nnode.data = string

    def exsit(self, string):
        # string 끝까지 노드를 탐색하면서, 끝에 도달했을때, data가 있으면 True 반환
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return False
        if nnode.data != None:
            return True
        else:
            return False

    def starts_with(self, prefix):
        # 해당 prefix까지 노드를 이동 -> BFS 탐색시도
        res = []
        nnode = self.head
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return res
        q = [nnode]
        while q:
            now = q.pop(0)
            if now.data != None:
                res.append(now.data)
            q += list(now.children.values())
        return res

    def starts_withL(self, string, L):
        # 해당 prefixe 까지 노드를 이동한다.
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return 0
        return nnode.lengths[L]


"""
이 트라이 자료구조의 한계 >중복된 입력에 대해서 lengths가 업데이트되지만 > 트리는 그대로 이다.
"""
mainTrie = Trie()
a = ['', 'a', 'b', 'c', 'ab', 'ac', 'ad', 'ta', 'abc', 'abcd']
b = ['', 'a', 't', 'ab']

for e in a:
    mainTrie.insert(e)

for e in b:
    print(mainTrie.exsit(e))
for e in b:
    print(mainTrie.starts_with(e))
for e in b:
    print(mainTrie.starts_withL(e, 2))
