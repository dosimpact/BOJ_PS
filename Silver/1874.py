from copy import deepcopy
import sys
import math


def input(): return sys.stdin.readline().rstrip()


N = int(input())
want = []
wantPointer = 0
for _ in range(N):
    i = int(input())
    want.append(i)
idx = 1  # 1부터 넣어서 N까지 stack에 넣을꺼임.
stack = []  # 스택이다
ans = []
while True:

    if idx > N:
        break
    # 만약, stack이 있고, 내가 원하는 숫자가 뺀위야, 그럼 가져와. 다음 원하는거
    if stack and want[wantPointer] == stack[-1]:
        stack.pop()
        ans.append('-')
        wantPointer += 1
        continue
    # 원하는 경우가 없어.
    stack.append(idx)
    ans.append('+')
    idx += 1


while stack:
    if want[wantPointer] == stack[-1]:
        ans.append('-')
        stack.pop()
        wantPointer += 1
    else:
        break

if stack:
    print("NO")
else:
    print(*ans)
