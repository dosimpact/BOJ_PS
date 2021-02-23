# import sys
# import math
# import re
# from typing import *
# import heapq

# input = sys.stdin.readline

# sys.setrecursionlimit(10 ** 6)

# 모듈이 단어의 첫 번째 글자를 추론하지는 않는다


class Node(object):
    def __init__(self, key, cnt=0, data=None):
        self.key = key
        self.data = data
        self.cnt = cnt
        self.children = {}

    def __str__(self):
        return f"key {self.key} data {self.data} "


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string: str):
        p: Node = self.head
        p.cnt += 1
        for s in string:
            if s not in p.children:
                p.children[s] = Node(s, 0)
            p = p.children[s]
            p.cnt += 1
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

    def start_with_common(self, prefix: str):
        p: Node = self.head
        for s in prefix:
            if s not in p.children:
                return prefix
            p = p.children[s]
        maxDepth = p.cnt
        q = [p]
        ans = prefix
        while q:
            now_node = q.pop(0)
            for key in now_node.children:
                if now_node.children[key].cnt == maxDepth:
                    ans += key
                    q.append(now_node.children[key])
        return ans


while True:
    try:
        T = int(input())
        data = [input().strip() for _ in range(T)]
        mainTrie = Trie()
        for d in data:
            mainTrie.insert(d)
        ans = [0 for _ in range(T)]
        for i in range(T):
            nowData = data[i]
            nowTmp = ""
            cntTmp = 0
            while True:
                if nowData == nowTmp:
                    break
                else:
                    nowTmp += nowData[len(nowTmp)]
                    res = mainTrie.start_with_common(nowTmp)
                    cntTmp += 1
                    if len(nowTmp) < len(res):
                        nowTmp = res

            ans[i] = cntTmp
        print("%.2f" % (sum(ans) / len(ans)))
    except:
        break
