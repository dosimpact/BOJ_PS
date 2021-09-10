import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


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
        nnode = self.head
        # 해당 문자열만큼 자식노드를 만들고  중간에 길이정보를 추가 | 마지막에 data 정보도 추가
        nnode.lengths[len(string)] += 1
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
            nnode.lengths[len(string)] += 1
        nnode.data = string

    def exist(self, string):
        nnode = self.head
        # string을 추적하여 끝에 도달한다. | 중간에 없다면 False | 마지막에 data가 없다면 False 외 True
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
        # prefix를 추적하여, 끝까지 도달 | 중간에 없다면 빈 배열 출력 | 그다음부터는 BFS 탐색으로 data있으면 res에 추가
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return res
        q = [nnode]
        while q:
            cnode = q.pop(0)
            if cnode.data != None:
                res.append(cnode.data)
            q += list(cnode.children.values())
        return res

    def starts_withLen(self, prefix, L: int):
        nnode = self.head
        # prefix를 추적하여, 끝까지 도달 | 중간에 없다면 빈 배열 출력 | 그다음부터는 BFS 탐색으로 data있으면 res에 추가
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return 0
        return nnode.lengths[(L)]


def solution(words, queries):
    answer = []
    FTree = Trie()
    BTree = Trie()
    for e in words:
        FTree.insert(e)
        BTree.insert(e[::-1])
    for e in queries:
        if e[0] == e[-1] == "?":
            answer.append(FTree.head.lengths[len(e)])
        elif e[0] == "?":
            answer.append(BTree.starts_withLen(e.replace("?", "")[::-1], len(e)))
        elif e[-1] == "?":
            answer.append(FTree.starts_withLen(e.replace("?", ""), len(e)))

    return answer
