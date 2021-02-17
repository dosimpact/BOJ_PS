import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dq = deque()

for i in range(T):
    coms = input().split()
    if coms[0] == "push":
        dq.append(coms[1])
    if coms[0] == "pop":
        print(dq.popleft()) if dq else print(-1)
    if coms[0] == "front":
        print(dq[0]) if dq else print(-1)
    if coms[0] == "back":
        print(dq[-1]) if dq else print(-1)
    if coms[0] == "size":
        print(len(dq))
    if coms[0] == "empty":
        print(0) if dq else print(1)
