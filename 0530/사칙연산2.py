
import sys


def input(): return sys.stdin.readline().rstrip()


# - 는 앞으로의 연산에+.- 를 두개 만든느 effect를 가진다.
# 하지만, - 이후 - 하나더 나왔을때 대처를 어떻게 ? , effect 상쇄 ? effect 더블 영향?

# 데이터는 원본, e 는 갯수만큼

class Node:
    def __init__(self, data=0, effect=0):
        self.data = data
        self.effect = effect
        self.child = []
        self.res = 0  # 나까지의 연산 결과
        self.buffer = 0  # 부모가 전달해준 연산결과


class Graph:
    def __init__(self):
        self.head = Node(0, 0)
        self.result = []
        self.leafNode = [self.head]

    # 노드   추가 : -15
    def addNode(self, data):
        newLeaf = []
        data = int(data)
        for nnode in self.leafNode:
            # 연산
            if nnode.effect % 2 == 0:
                nnode.res = nnode.buffer + nnode.data
            else:
                nnode.res = nnode.buffer - nnode.data
            # 확장
            newNodeList = []
            if nnode.data < 0 and nnode.effect == 0:
                n1 = Node(data, nnode.effect)
                n2 = Node(data, nnode.effect+1)
                newNodeList = [n1, n2]

            if nnode.data < 0 and nnode.effect > 0:
                n1 = Node(data, nnode.effect)
                n2 = Node(data, nnode.effect+1)
                n3 = Node(data, nnode.effect-1)
                newNodeList = [n1, n2, n3]

            if nnode.data >= 0 and nnode.effect == 0:
                n1 = Node(data, nnode.effect)
                newNodeList = [n1]

            if nnode.data >= 0 and nnode.effect > 0:
                n1 = Node(data, nnode.effect)
                n2 = Node(data, nnode.effect-1)
                newNodeList = [n1, n2]

            for n in newNodeList:
                newLeaf.append(n)
                nnode.child.append(n)
                n.buffer = nnode.res
        self.leafNode = newLeaf

    def updateResult(self):
        for nnode in self.leafNode:
            # 연산
            if nnode.effect % 2 == 0:
                nnode.res = nnode.buffer + nnode.data
            else:
                nnode.res = nnode.buffer - nnode.data
        for n in self.leafNode:
            self.result.append(n.res)
        # self.result = list(map(self.leafNode, lambda n: n.res))
        pass


def solution(arr):
    g = Graph()
    g.addNode(arr[0])
    for i in range(1, len(arr), 2):  # 7 | 0 12 34 56
        g.addNode("".join(arr[i:i+2]))
    g.updateResult()
    return max(g.result)


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", '4']))
