class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)
    """
    기능 삽입, 존재성, prefixe 검색
    """

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
