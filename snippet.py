"""

"""


from collections import defaultdict


class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
        self.lens = defaultdict(int)


class Trie:
    def __init__(self):
        self.head = Node(None)

    # 삽입
    def insert(self, string):
        nnode = self.head
        for s in string:  # abc
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
        nnode.data = string

    def exists(self, string):
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return False
        if nnode.data == string:
            return True
        else:
            return False

    def search(self, prefix):
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


mainTrie = Trie()
a = ['', 'a', 'ab', 'abc', 't', 'ta']
for e in a:
    mainTrie.insert(e)
b = ['', 'a', 't', 'kk']

for e in b:
    print(mainTrie.exists(e))
for e in b:
    print(mainTrie.search(e))
