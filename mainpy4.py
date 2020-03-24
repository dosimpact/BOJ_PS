
import sys

DEBUG = False


def input(): return sys.stdin.readline().rstrip()


SIZE = 10
k = 0

res = sys.stdin.read()
res = list(map(int, res.split()))


iinputs = [[] for _ in range(res.count(0)//2)]

now = 0
while len(res) != 0:
    here = res.pop(0)
    if here == -1:
        break
    elif here != 0:
        iinputs[now].append(here)
    elif here == 0:
        now += 1
        res.pop(0)


for inpu in iinputs:
    k += 1
    inputs = inpu

    if DEBUG:
        print("-->1 inputs", inputs)
    outdeg = [[] for _ in range(SIZE)]
    indeg = [[] for _ in range(SIZE)]
    nodes = []

    for i in range(0, len(inputs), 2):
        outdeg[inputs[i]].append(inputs[i+1])
        indeg[inputs[i+1]].append(inputs[i])
        nodes.append(inputs[i])
        nodes.append(inputs[i+1])
    nodes = list(set(nodes))
    if DEBUG:
        print("-->2 nodes out,in deg", nodes, outdeg, indeg)

    isposs = True

    root = -1
    # 루트의 갯수가 1개이어야한다.
    for node in nodes:
        if len(indeg[node]) == 0:
            if root == -1:
                root = node
            else:
                isposs = False
    # 인디그리가 2개이상인건 업성야 한다.
    for node in nodes:
        if len(indeg[node]) >= 2:
            isposs = False
    if isposs:
        print(f'Case {k} is a tree.')
    else:
        print(f'Case {k} is not a tree.')

"""

6 8  5 3  5 2  6 4 


5 6  0 0
0 0
0 0


8 1  7 3 
 6 2  8 
 9  7 5
7 4  7 8  7
 6  
 0 0

3 8  6 8  6 4
5 3  5 6  5 2  0 
0
-1 -1

fb)너무 어렵게 푸는거 아닌가?
"""
