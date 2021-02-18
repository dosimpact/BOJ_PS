import sys
from typing import *

input = sys.stdin.readline


N: int = int(input())
graph: List[List[str]] = [list(input().strip()) for _ in range(N)]  # 인접리스트
ans = []


for i in range(N):
    check = [-1 for _ in range(N)]
    check[i] = 0  # 나는 0 , 1 , 2촌까지 검색
    q = [i]
    data = 0
    while q:
        now = q.pop(0)
        for nxt in range(N):
            if graph[now][nxt] == "Y" and check[nxt] == -1:
                if check[now] <= 1:
                    check[nxt] = check[now] + 1
                    q.append(nxt)
                    data += 1
    ans.append(data)

print(max(ans))

"""
4
NYNN
YNYN
NYNY
NNYN


6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN
"""