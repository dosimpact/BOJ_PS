from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None) -> None:
        self.key = key
        self.data = data
        self.children = {}
        self.lengths = defaultdict(int)


class Trie(object):
    def __init__(self) -> None:
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        cur_node.lengths[len(string)] += 1

        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)
            cur_node = cur_node.children[s]
            cur_node.lengths[len(string)] += 1
        cur_node.data = string

    def starts_withLen(self, string, depth):
        cur_node = self.head
        # string 접두사까지 노드포인터를 이동시킨다.
        for s in string:
            if s not in cur_node.children:
                return 0
            cur_node = cur_node.children[s]
        # 도중 없다면 0 반환
        return cur_node.lengths[depth]


def solution(words, queries):
    result = []
    # prefixTree = Trie()
    # subfixTree = Trie()
    dict_prefixTree = defaultdict(Trie)
    dict_subfixTree = defaultdict(Trie)

    for w in words:
        dict_prefixTree[len(w)].insert(w)
        dict_subfixTree[len(w)].insert(w[::-1])
    for q in queries:
        if q[0] == q[-1] == "?":
            result.append(dict_prefixTree[len(q)].head.lengths[len(q)])
        elif q[-1] == "?":
            qidx = q.index("?")
            # res = prefixTree.starts_withLen(q[:qidx], len(q))
            # res = prefixTree.starts_withLen(q.replace("?", ""), len(q))
            res = dict_prefixTree[len(q)].starts_withLen(q[:qidx], len(q))
            # print(res)
            result.append((res))
        elif q[0] == "?":
            q = q[::-1]
            qidx = q.index("?")
            # res = subfixTree.starts_withLen(q[:qidx], len(q))
            # res = subfixTree.starts_withLen(q.replace("?", "")[::-1], len(q))
            res = dict_subfixTree[len(q)].starts_withLen(q[:qidx], len(q))
            # print(res)
            result.append((res))
    return result


# 접두사 검색인 경우 , 접미사 검색인 경우
# ??의 갯수만큼만 깊이 검색이 필요함

# print(
#     solution(
#         ["frodo", "front", "frost", "frozen", "frame", "kakao"],
#         ["fro??", "????o", "fr???", "fro???", "pro?"],
#     )
# )

