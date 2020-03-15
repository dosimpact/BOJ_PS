import sys


def input(): return sys.stdin.readline().strip()


N = int(input())
towerinput = input().split()
tow = []

for i, t in enumerate(towerinput):
    tow.append([i+1, int(t)])

stack = []
Ans = []
for i in range(len(tow)):
    #print("--> i tow", i, tow, stack)
    # 스택이 비어있는경우 | 수진자 없고 내가 스택
    if len(stack) == 0:
        stack.append(tow[i])
        Ans.append(0)
    # 스택이 있는경우 | 스택의 탑이 나보다 큰 경우 조용히 Ans에 들어가
    else:
        if stack[-1][1] > tow[i][1]:
            Ans.append(stack[-1][0])
            stack.append(tow[i])
        else:
            # 스택이 있고 나보다 작다면, 나보다 큰녀속이 나올때까지 pop하기
            #print("--> tow[i][1]", tow[i][1])
            while(stack[-1][1] < tow[i][1] and len(stack) != 0):
                stack.pop()
                if len(stack) == 0:
                    Ans.append(0)
                    break
            if len(stack) != 0:
                Ans.append(stack[-1][0])
            stack.append(tow[i])


for an in Ans:
    print(an, end=" ")
