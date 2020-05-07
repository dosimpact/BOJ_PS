import sys


def input(): return sys.stdin.readline().rstrip()


def mergeSort(ori: []):
    # BC
    if len(ori) <= 1:
        return
    # 분할 | merge recursion
    head = ori[:len(ori)//2]
    tail = ori[len(ori)//2:]
    mergeSort(head)
    mergeSort(tail)
    # 정복 | logic
    i, j, k = 0, 0, 0  # head, tail, ori 에 대한 포인터(사실 인덱스)
    while i < len(head) and j < len(tail):
        if head[i] < tail[j]:
            ori[k] = head[i]
            i += 1
        else:
            ori[k] = tail[j]
            j += 1
        k += 1
    while i < len(head):
        ori[k] = head[i]
        k += 1
        i += 1
    while j < len(tail):
        ori[k] = tail[j]
        k += 1
        j += 1


arr = [6, 15, 4, 1, 5, 5, 5, 29, 2, 3, 0]

print(arr)
mergeSort(arr)
print(arr)
