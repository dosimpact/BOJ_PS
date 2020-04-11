
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


"""
인덱스 선택 | 비내림차임 | 중복인덱스 가능 | 결과는 중복제거
"""

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
SIZE = 8

check = [False]*SIZE
IList = [0]*SIZE
Ans = []


def go(idx: int, sIdx: int):
    if idx == M:
        tmp = [data[i] for i in IList[:M]]
        Ans.append(tuple(tmp))
        return

    for i in range(sIdx, N):
        # if check[i]:
        #     continue
        check[i], IList[idx] = True, i
        go(idx+1, i)
        check[i] = False


go(0, 0)
Ans = list(set(Ans))
Ans.sort()
print(Ans)
for i in range(len(Ans)):
    print(*Ans[i])
"""
Input :
4 4
1 1 2 2

4 4
1 1 2 2
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2

4 4
1 1 2 2
[(1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 2), (1, 2, 2, 2), (2, 2, 2, 2)]
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2

"""
