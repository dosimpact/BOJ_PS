from sys import stdin, setrecursionlimit
from collections import deque

input = stdin.readline
setrecursionlimit(10 ** 6)


class Node(object):
    def __init__(self, parent, name):
        self.child = dict()
        self.parent = parent  # Node Ref
        self.name = name
        self.price = 0
        return


class Trie(object):
    def __init__(self):
        self.head = Node(None, "center")
        self.NodeList = dict()
        self.NodeList["center"] = self.head
        return

    def insert(self, name):
        self.NodeList[name] = Node(None, name)

    def mapping(self, p: str, c: str):
        self.NodeList[p].child[c] = self.NodeList[c]
        self.NodeList[c].parent = self.NodeList[p]

    def query(self, leaf, price):
        q = [self.NodeList[leaf]]  # 방문예정, 방문시 돈을 줄거임
        while q:
            now = q.pop(0)
            price_10 = price / 10
            if int(price_10) != price_10:
                now.price += price
                break
            else:
                price_10 = int(price_10)
            now.price += price_10 * (9)  # 20원 -> 18+2원
            price = price_10
            if now.parent:
                q.append(now.parent)
        return price

    def getPrice(self, enroll):
        res = []
        for e in enroll:
            res.append(self.NodeList[e].price)
        return res


def solution(enroll, referral, seller, amount):
    mainTrie = Trie()

    for e in enroll:
        mainTrie.insert(e)

    for c, p in zip(enroll, referral):
        if p == "-":
            mainTrie.mapping("center", c)
        else:
            mainTrie.mapping(p, c)

    for leaf, amt in zip(seller, amount):
        mainTrie.query(leaf, amt * 100)
    res = mainTrie.getPrice(enroll)
    res = list(map(int, res))
    return res


# 구성원들
# 부모가 누구인지
# 판매 - 판매액 매핑 테이블
res = solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10],
)
print(res)