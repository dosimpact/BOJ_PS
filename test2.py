from copy import deepcopy
import sys
import math


def input(): return sys.stdin.readline().rstrip()


N = int(input())
wntList = []
for _ in range(N):
    e = int(input())
    wntList.append(e)
wPointer = 0

producer = 1
stack = []
ans = []
while True:
    #print(producer, stack, ans)
    # 갈망
    if stack and stack[-1] == wntList[wPointer]:
        ans.append('-')
        stack.pop()
        wPointer += 1
        continue

    # 충족
    if producer <= N:
        stack.append(producer)
        producer += 1
        ans.append('+')
        continue
    # 욕먕
    if producer > N and stack and stack[-1] != wntList[wPointer]:
        break
    if producer > N and len(stack) == 0:
        break

if stack:
    print('NO')
else:
    for a in ans:
        print(a)
