import sys


def input(): return sys.stdin.readline().rstrip()


def mergeSort(ori: []):  # ori 배열을 ,오름차순으로 정렬을 한다.
    if len(ori) <= 1:
        return

    mid = len(ori)//2
    head = ori[:mid]
    tail = ori[mid:]
    mergeSort(head)  # [6, 15, 4, 1, 5,] >    4 5  6 15
    mergeSort(tail)  # [5, 29, 2, 3, 0] >      29
    # 0 1 2 3  4 5 5 ... 29
    i, j, k = 0, 0, 0
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
        i += 1
        k += 1

    while j < len(tail):
        ori[k] = tail[j]
        j += 1
        k += 1


arr = [6, 15, 4, 1, 5, 29, 2, 3, 0]
mergeSort(arr)
print(arr)


"""
재귀함수로 구현됨.
구성
1. BC Stop : 크기가 1이하인 배열이 있다면, 그냥 리턴
2. 분할 > 재귀함수 : 배열을 두개로 나누어서, 잘 알아서 각자 정렬하고 와
3. 그 결과를 > 정복 > 로직컬 처리 : 그러면 두개의 배열을 합치는 로직

증명 수학적 귀납법?

Mergetsort는 배열을 정렬하여 리턴.

1. 배열의 길이가 1일때 > 기저경우에 의해서 항상 참
2. 배열의 길이가 head,tail 이 k일때, 두 배열은 정렬이 되었음을 가정 > k+1 인상황에도 정렬이 되었다.
3. 1과 2에 의해, 모든 배열의 길이에 대해, 정렬이 완성 된다.
"""
