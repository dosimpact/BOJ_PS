# 트라이 자료구조
import sys


class Node(object):
    def __init__(self, key, data=None):
        self.key: str = key
        self.data: str = data
        self.children: {} = {}


class Trie(object):

    def __init__(self):
        self.head = Node(None)  # 첫노드의 key 값은 ? 사실상 없어도 되는데.

    def insert(self, string: str):
        nnode = self.head
        # string의 모든 문자열에 대한 노드를 만든다. cross | 만약에 자식노드에 해당 key값으로 노드가 없다면, 만들어준다. | 다음 노드로
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
        nnode.data = string

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
            q += list(now.children.values())
        return ans


def solution(words, queries):
    frontTrie = Trie()
    backTrie = Trie()

    for w in words:
        frontTrie.insert(w)
        backTrie.insert(w[::-1])

    answer = []

    for q in queries:
        if word == "?"*len(q):
            answer.append

        if q[0] == "?":
            res = backTrie.starts_with(q.replace("?", ""))
            print(f"De > {res}")
            if res:
                answer.append(
                    len(list(filter(lambda e: len(e) == len(q), res))))
            else:
                answer.append(0)
        else:
            res = frontTrie.starts_with(q[:q.index("?")])
            print(f"De > {res}")
            if res:
                answer.append(
                    len(list(filter(lambda e: len(e) == len(q), res))))
            else:
                answer.append(0)

    return answer


a = ["f", "fr", "fe", "frodo", "front", "frost", "frozen", "frame", "kakao"]
b = ["?", "??", "?????", "??????", "fr???", "fr????", "pro?", "??odo", "fro??"]
print(solution(a, b))
