import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


dq = deque(list(input()))
n = int(input())
dq2 = deque()

for _ in range(n):
    a, *b = input().split()
    if a == 'L':
        if len(dq) != 0:
            dq2.appendleft(dq.pop())
    if a == 'D':
        if len(dq2) != 0:
            dq.append(dq2.popleft())
    if a == 'B':
        if len(dq) != 0:
            dq.pop()
    if a == 'P':
        dq.append(b[0])


for e in list(dq):
    print(e, end='')
for e in list(dq2):
    print(e, end='')
