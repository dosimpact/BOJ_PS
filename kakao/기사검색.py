from collections import defaultdict


class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = None
        self.nexts = {}
        self.lengths = defaultdict(int)


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curNode = self.head
        curNode.lengths[len(string)] += 1
        for s in string:
            if s not in curNode.nexts:
                curNode.nexts[s] = Node(s)
            curNode = curNode.nexts[s]
            curNode.lengths[len(string)] += 1
        curNode.data = string

    def search(self, string):
        curNode = self.head
        for s in string:
            if s in curNode.nexts:
                curNode = curNode.nexts[s]
            else:
                return False
        if curNode.data != None:
            return True
        else:
            return False

    def starts_with(self, prefix):
        curNode = self.head
        for s in prefix:
            if s in curNode.nexts:
                curNode = curNode.nexts[s]
            else:
                return None
        q = [curNode]
        res = []
        while q:
            nnode = q.pop()
            if nnode.data != None:
                res.append(nnode.data)
            q += list(nnode.nexts.values())

        return res

    def starts_withLen(self, prefix, L: int):
        curNode = self.head
        for s in prefix:
            if s in curNode.nexts:
                curNode = curNode.nexts[s]
            else:
                return 0

        return curNode.lengths[L]


def solution(words, queries):
    answer = []
    frontTree = Trie()
    backTree = Trie()
    for word in words:
        frontTree.insert(word)
        backTree.insert(word[::-1])

    for word in queries:
        if word == "?"*len(word):
            answer.append(frontTree.head.lengths[len(word)])
        elif word[0] == "?":
            prefix = word[::-1].split("?")[0]
            res = backTree.starts_withLen(prefix, len(word))
            answer.append(res)
        elif word[-1] == "?":
            res = frontTree.starts_withLen(word.replace("?", ""), len(word))
            answer.append(res)

    return answer
