import sys
import math
import re
from typing import *
import heapq

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
# 전화번호부 일관성
# 911
# 91125
# 911밑에 서브셋이 없는경우

# 911 검색결과 서브셋이 없어야 한다. - Tire 예제


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def __str__(self):
        return f"key {self.key} data {self.data} "


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string: str):
        p: Node = self.head
        for s in string:
            if s not in p.children:
                p.children[s] = Node(s)
            p = p.children[s]
        p.data = string

    def search(self, prefix: str):
        p: Node = self.head
        for s in prefix:
            if s not in p.children:
                return False
            p = p.children[s]
        if p.data == prefix:
            return True
        else:
            return False

    def start_with(self, prefix: str):
        p: Node = self.head
        for s in prefix:
            if s not in p.children:
                return []
            p = p.children[s]
        q = list(p.children.values())
        ans = []
        while q:
            now_node = q.pop(0)
            if now_node.data != None:
                ans.append(now_node.data)
            q += list(now_node.children.values())
        return ans

    def inorder(self, node: Node, depth: int):
        # print(f"[{depth}]{node.data[-1]}")
        if node.data:
            print(f"{'--'*depth}{node.data[-1]}")
        keys = list(node.children.keys())
        keys.sort()
        for key in keys:
            self.inorder(node.children[key], depth+1)

    # 또 같은 층에 여러 개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온다.)


main = Trie()
N = int(input())
for _ in range(N):
    data = list(input().split())
    data = data[1:]
    # for i in range(len(data)):
    # insData = "".join(data[:i+1])
    # print(f"insData {insData}")
    # main.insert(insData)
    for i in range(len(data)):
        insData = (data[:i+1])
        main.insert(insData)
    # print(main.start_with([]))
main.inorder(main.head, -1)
