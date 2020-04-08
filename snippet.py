"""
-트라이 자료구조 구현하기
-행렬 회전하기 시계방향 90됴 ( 노말버전, 파이썬 버전 )
-다음 순열 구현하기
-gcd,LG 구현하기
"""
from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.lengths = defaultdict(int)


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        nnode = self.head
        nnode.lengths[len(string)] += 1

        for s in string:  # H > cross
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
            nnode.lengths[len(string)] += 1
        nnode.data = string

    def exist(self, string):
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
        nnode = self.head
        res = []
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return res
        q = [nnode]
        while q:
            now = q.pop()
            if now.data != None:
                res.append(now.data)
            q += list(now.children.values())
        return res

    def starts_withLen(self, prefix, L: int):
        nnode = self.head
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return 0
        return nnode.lengths[L]


# mainTrie = Trie()
# a = ["a", "b", "c", "ab", "ac", "ad", "abcd"]
# b = ["", "a", "ab", "ae", "e"]
# for e in a:
#     mainTrie.insert(e)
# for e in b:
#     print(mainTrie.starts_with(e))
# for e in b:
#     print(mainTrie.starts_withLen(e, 2))


def solution(words, queries):
    answer = []
    FTree = Trie()
    BTree = Trie()
    for w in words:
        FTree.insert(w)
        BTree.insert(w[::-1])
    for w in queries:
        if w[0] == "?" and w[-1] == "?":
            answer.append(FTree.head.lengths[len(w)])
        elif w[-1] == "?":
            answer.append(FTree.starts_withLen(w.replace("?", ""), len(w)))
        elif w[0] == "?":
            tmpW = w.replace("?", "")[::-1]
            answer.append(BTree.starts_withLen(tmpW, len(w)))
    return answer
