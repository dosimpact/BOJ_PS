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

    def insert(self):
        pass

    def search(self, string):
        pass

    def starts_with(self, prefix):
        pass
