# Trie 자료구조


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self) -> None:
        self.head = Node(None)

    # 받은 문자열만큼 노드를 생성한다.
    def insert(self, string):
        # 현재 노드는 헤드 부터 시작해서, 받은 문자열을 모두 노드에 넣는다.
        # 만약 이미 같은 key값을 가진 노드가 있다면 건너 뛴다.
        cur_node = self.head
        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)
            cur_node = cur_node.children[s]
        cur_node.data = string
        print(string, "is insert")

    def search(self, string):
        # 문자열을 순회하면서, 자식노드로 탐색을 진행한다. , 없다면 False 출력
        cur_node = self.head
        for s in string:
            if s in cur_node.children:
                cur_node = cur_node.children[s]
            else:
                return False
        if cur_node.data == string:
            return True
        else:
            return False

    # 접두사로 시작하는 단어들을 모두 찾는다.
    def startsWith(self, string):
        result = []
        cur_node = self.head
        # 해당 접두사까지 이동을 한다. 해당 접두사로 시작하는 단어가 아예 없다면 빈 배열을 리턴
        for s in string:
            if s in cur_node.children:
                cur_node = cur_node.children[s]
            else:
                return result
        # 접두사까지 자식 노드의 탐색위치로 이동하고, 순회를 거처 (큐이용) 배열을 리턴
        q = [cur_node]  # list<노드 객체>
        while q:
            now = q.pop(0)
            if now.data:
                result.append(now.data)
            q += list(now.children.values())
        return result


trie = Trie()
for ss in ["hello", "helloworld", "hell"]:
    trie.insert(ss)
# for ss in ["hello", "helloworld", "hell", "he"]:
# print(trie.search(ss))
print(trie.startsWith("h"))
print(trie.startsWith(""))
print(trie.startsWith("hello"))
