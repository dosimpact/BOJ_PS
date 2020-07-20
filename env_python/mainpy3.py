"""
D 두배,9999보다크면 나머지
S -1, 0이라면 9999저장
L 왼편회전
E 오른편 회전

A->B의 최소 명령.

문자열로
1000 > 0001

* check를 "" > "D" > "DL" > "DLS" > "DLSS" ... 힘들어
=> fromNode 배열로 물어보자. 너 어디서 왔니?
"""

import sys


def input(): return sys.stdin.readline().rstrip()


def sol():
    LIMIT_N = 10001
    A, B = map(int, input().split())
    
    check[A] = 0

    q = [[A, ""]]
    while q:
        now, trace = q.pop(0)
        if now == B:
            return trace
        tmp = (now*2) % 10000
        if check[tmp] == -1:
            check[tmp] = check[now] + 1
            q.append([tmp, trace+"D"])

        tmp = 9999 if now == 0 else now-1
        if check[tmp] == -1:
            check[tmp] = check[now] + 1
            q.append([tmp, trace+"S"])

        tmp = (now % 1000)*10 + now//1000
        if check[tmp] == -1:
            check[tmp] = check[now] + 1
            q.append([tmp, trace+"L"])

        tmp = (now % 10)*1000 + now // 10
        if check[tmp] == -1:
            check[tmp] = check[now] + 1
            q.append([tmp, trace+"R"])


case = int(input())
for _ in range(case):
    print(sol())

"""

0 9999
0 1
"""
