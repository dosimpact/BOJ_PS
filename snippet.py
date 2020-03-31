
# https://www.acmicpc.net/problem/6416

import sys
import math
import functools
import itertools

DEBUG = False


sys.setrecursionlimit(10**6)


# def input(): return sys.stdin.readline().rstrip()


buf = sys.stdin.read()
buf = list(map(int, buf.split()))
k = 0

indegCnt = {}
nodes = []
linecnt = 0
graph = {}
while True:
    u = buf.pop(0)
    v = buf.pop(0)

    if u == -1:
        break
    if u == 0 and v == 0:
        k += 1
        nodes = list(set(nodes))

        # 루트 찾기
        isposs = True
        root = 0
        for key in indegCnt:
            if indegCnt[key] == 0:
                if root == 0:
                    root = key
                else:
                    isposs = False
            elif indegCnt[key] == 1:
                pass
            else:
                isposs = False
        if root == 0:
            isposs = False

        if not isposs:
            print(f'Case {k} is not a tree.')
        else:
            # 탐색
            nodeNums = []
            for num in graph:
                nodeNums.extend(graph[num])
                nodeNums.append(num)
            nodeNums = list(set(nodeNums))
            isCheck = {}
            for num in nodeNums:
                isCheck[num] = 0
            # print(isCheck)
            # print('root', root)
            # print(graph)
            isCheck[root] = 1
            q = []
            q.append(root)
            while len(q) >= 1:
                current = q.pop(0)

                if current not in graph:
                    continue
                for next in graph[current]:
                    if isCheck[next] == 0:
                        isCheck[next] = 1
                        q.append(next)
                    else:
                        isposs = False
            for key in isCheck:
                if isCheck[key] == 0:
                    isposs = False
            if isposs:
                print(f'Case {k} is a tree.')
            else:
                print(f'Case {k} is not a tree.')

        # if len(nodes) == 0 or len(nodes)-1 == linecnt:
        #     print(f'Case {k} is a tree.')
        # else:
        #     print(f'Case {k} is not a tree.')
        graph.clear()
        nodes.clear()
        linecnt = 0
        indegCnt.clear()
    else:
        linecnt += 1
        nodes.append(u)
        nodes.append(v)
        # u > v
        if v not in indegCnt:
            indegCnt[v] = 1
        else:
            indegCnt[v] += 1
        if u not in indegCnt:
            indegCnt[u] = 0
        else:
            pass
        # u > v 인접리스트
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
"""
6 8  5 3  5 2  6 4
5 6  0 0

8 1  7 3  6 2  8 9  7 5
7 4  7 8  7 6  0 0

3 8  6 8  6 4
5 3  5 6  5 2  0 0

1 2  1 3  0 0

2 1  3 1  0 0

1 2  2 3  3 1  4 5  0 0

4 5 0 0

1 2 2 3 3 1 0 0

-1 -1

"""
