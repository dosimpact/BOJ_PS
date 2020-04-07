class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """

    def insert(self, string):
        curr_node = self.head

        for char in string:  # 해당 문자열을 돌면서
            if char not in curr_node.children:  # 키값으로 해당 자식이 없다면
                curr_node.children[char] = Node(char)  # key - value로 연결

            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string

    """
    주어진 단어 string이 트라이에 존재하는지 여부를 반환합니다.
    """

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # string의 마지막 글자에 다달았을 때,
        # curr_node 에 data 가 있다면 string이 트라이에 존재하는 것!
        if (curr_node.data != None):
            return True
        else:
            return False

    """
    주어진 prefix 로 시작하는 단어들을
    트라이에서 찾아 리스트 형태로 반환합니다.
    """

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        # 트라이에서 prefix 를 찾고,
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return None
        # bfs 로 prefix subtrie를 순회하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        #queue = list(subtrie.children.values())
        queue = [curr_node]
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            queue += list(curr.children.values())

        return result
