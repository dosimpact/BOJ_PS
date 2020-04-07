# 트라이 자료구조


class Node(object):
    def __init__(self, key=None, data=None):
        self.key: str = key
        self.data: str = data
        self.children: {} = {}


class Trie(object):

    def __init__(self):
        self.head = Node()  # 첫노드의 key 값은 ? 사실상 없어도 되는데.

    def insert(self, string: str):
        nnode = self.head
        # string의 모든 문자열에 대한 노드를 만든다. cross | 만약에 자식노드에 해당 key값으로 노드가 없다면, 만들어준다. | 다음 노드로
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
        nnode.data = string

    def search(self, string: str):
        # 존재성
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

    def starts_with(self, prefix: str):
        # 접두사 체크
        nnode = self.head

        # 접두사 까지 노드 진행

        for pre in prefix:
            if pre in nnode.children:
                nnode = nnode.children[pre]
            else:
                return None
        q = [nnode]
        ans = []
        while q:
            now = q.pop()
            if now.data:
                ans.append(now.data)
            for key in now.children:
                q.append(now.children[key])
        return ans


mainTrie = Trie()
mainTrie.insert("cross")
mainTrie.insert("crossxx")
mainTrie.insert("crosx")
mainTrie.insert("tross")
print(mainTrie.search("cross"))
print(mainTrie.search("xross"))
print(mainTrie.search("crossx"))
print(mainTrie.starts_with("cross"))
print(mainTrie.starts_with("x"))
print(mainTrie.starts_with("t"))
print(mainTrie.starts_with("cro"))
