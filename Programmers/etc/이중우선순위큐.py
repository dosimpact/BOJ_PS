

import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


"""


"""


# def solution(operations):
#     heap = []
#     heapq.heapify(heap)
#     for operation in operations:
#         operator, operand = operation.split(' ')
#         operand = int(operand)

#         if operator == 'I':
#             heapq.heappush(heap, operand)
#         elif heap:
#             if operand < 0:
#                 heapq.heappop(heap)
#             else:
#                 heap.remove(max(heap))

#     if not heap:
#         return [0, 0]

#     return [max(heap), heap[0]]


def solution(operations):
    q = []
    heapq.heapify(q)
    for op in operations:
        o, su = op[0], int(op[2:])
        if o == "I":
            heapq.heappush(q, su)
        elif q:
            if su == 1:
                q.remove(max(q))
            else:
                heapq.heappop(q)
    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]


# print(solution(	["I -45", "I 653", "D 1", "I -642","I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
