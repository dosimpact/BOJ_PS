"""
-R-A-M-

# 자주쓰는 알고리즘

-트라이 자료구조 구현하기 ✔
-행렬 회전하기 시계방향 90됴 ( 노말버전, 파이썬 버전 ) ✔
-다음 순열 구현하기 ✔
-gcd,LG 구현하기 ✔
-비트마스크로 모든 집합 순회하기 (1182 BOJ) ✔
"""

from collections import defaultdict


class Node(object):
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}
        self.lengths = defaultdict(int)


class Trie(object):
    def __init__(self):
        self.head = Node(None)


<< << << < HEAD
   def insert(self, string):
        # string 를 한바퀴 돌면서, node를 계속 연결해 준다.
        nnode = self.head
        nnode.lengths[len(string)] += 1
        for s in string:
            if s not in nnode.children:
                nnode.children[s] = Node(s)
            nnode = nnode.children[s]
            nnode.lengths[len(string)] += 1
        nnode.data = string

    def exsit(self, string):
        # string 끝까지 노드를 탐색하면서, 끝에 도달했을때, data가 있으면 True 반환
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return False
        if nnode.data != None:
            return True
        else:
            return False

    def starts_with(self, prefix):
        # 해당 prefix까지 노드를 이동 -> BFS 탐색시도
        res = []
        nnode = self.head
        for s in prefix:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return res
        q = [nnode]
        while q:
            now = q.pop(0)
            if now.data != None:
                res.append(now.data)
            q += list(now.children.values())
        return res

    def starts_withL(self, string, L):
        # 해당 prefixe 까지 노드를 이동한다.
        nnode = self.head
        for s in string:
            if s in nnode.children:
                nnode = nnode.children[s]
            else:
                return 0
        return nnode.lengths[L]


"""
이 트라이 자료구조의 한계 >중복된 입력에 대해서 lengths가 업데이트되지만 > 트리는 그대로 이다.
"""
mainTrie = Trie()
a = ['', 'a', 'b', 'c', 'ab', 'ac', 'ad', 'ta', 'abc', 'abcd']
b = ['', 'a', 't', 'ab']

for e in a:
    mainTrie.insert(e)

for e in b:
    print(mainTrie.exsit(e))
for e in b:
    print(mainTrie.starts_with(e))
for e in b:
    print(mainTrie.starts_withL(e, 2))
== =====


def input(): return sys.stdin.readline().rstrip()

"""
L R 
8808 8880
[L R]
8808 3
8809 2
"""

L, R = map(int, input().split())

# 큰자리수를 기준으로 돌리면 됨.
MAXLEN = max(len(str(L)), len(str(R)))
AnsMin = min(str(L).count("8"), str(R).count("8"))

IList = [0]*11
Data = ["7", "8", "9"]


def go(idx: int):
    global AnsMin
    if idx == MAXLEN:
        Tmp = [Data[k] for k in IList[:MAXLEN]]
        res = "".join(Tmp)
        resInt = int(res)

        if L <= resInt and resInt <= R:
            print(f"{res} -> {resInt} : {res.count('8')}")
            AnsMin = min(AnsMin, res.count('8'))
        return
    for i in range(0, 3):
        IList[idx] = i
        go(idx+1)


if AnsMin == 0 or len(str(L)) != len(str(R)):
    print(0)
    exit(0)
else:
    Lt = list(str(L))
    Rt = list(str(R))
    j = 0
    for k in range(0, min(len(Lt), len(Rt))):
        if Lt[k] == Rt[k]:
            j += 1
        else:
            break
    Lt, Rt = Lt[j:], Rt[j:]
    print(Lt, Rt)
    MAXLEN = max(len(str(L)), len(str(R)))
    # go(0)

print(AnsMin)
>>>>>> > b1ad246343f6e6a0af4fcb71f282689de28227d7
