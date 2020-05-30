
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

    # 노드   추가 : -15
    def addNode(self, data):
        # 끝점까지 다 도달 > 추가하기
        data = int(data)
        q = [self.head]
        while q:
            nnode = q.pop(0)
            if len(nnode.child) == 0:
                if nnode.data < 0 and nnode.effect == 0:
                    nnode.child.append(Node(data, nnode.effect))
                    nnode.child.append(Node(data, nnode.effect+1))

                if nnode.data < 0 and nnode.effect > 0:
                    nnode.child.append(Node(data, nnode.effect-1))
                    nnode.child.append(Node(data, nnode.effect))
                    nnode.child.append(Node(data, nnode.effect+1))

                if nnode.data >= 0 and nnode.effect == 0:
                    nnode.child.append(Node(data, nnode.effect))

                if nnode.data >= 0 and nnode.effect > 0:
                    nnode.child.append(Node(data, nnode.effect))
                    nnode.child.append(Node(data, nnode.effect-1))
            else:
                q += nnode.child  # extends

    def updateResult(self):
        # dfs
        q = [self.head]
        while q:
            # 특정 노드를 꺼내. | 나까지 먼저 연산 > 자식 있으면 notice, 아니면 나까지의 연살 결과를 result 배열에 담기
            nnode = q.pop(0)
            if nnode.effect % 2 == 0:
                nnode.res = nnode.buffer + nnode.data
            else:
                nnode.res = nnode.buffer - nnode.data
            if len(nnode.child) != 0:
                for ch in nnode.child:
                    ch.buffer = nnode.res
                q += nnode.child
            else:
                self.result.append(nnode.res)


def solution(arr):
    g = Graph()
    g.addNode(arr[0])
    for i in range(1, len(arr), 2):  # 7 | 0 12 34 56
        g.addNode("".join(arr[i:i+2]))
    g.updateResult()
    print(g.result)
    return max(g.result)


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", '4']))
