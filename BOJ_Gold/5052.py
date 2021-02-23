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


T = int(input())
for _ in range(T):
    main = Trie()
    n = int(input())
    data = [input().strip() for _ in range(n)]
    for d in data:
        main.insert(d)
    isNo = False
    for d in data:
        res = main.start_with(d)
        if len(res) >= 1:
            print("NO")
            isNo = True
            break
    if not isNo:
        print("YES")
