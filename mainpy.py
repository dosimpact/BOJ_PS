from collections import deque

dq = deque()

t = int(input())

for i in range(t):
    cmd = input().split()
    if(cmd == 'push_front'):
        x = int(input())
        dq.append(x)

    if(cmd == 'push_back'):
        x = int(input())
        dq.appendleft(x)

    if(cmd == 'pop_front'):
        if(len(dq) == 0):
            print(-1)
            break
        print(dq.popleft())

    if(cmd == 'pop_back'):
        if(len(dq) == 0):
            print(-1)
            break
        print(dq.pop())

    if(cmd == 'size'):
        print(len(dq))

    if(cmd == 'empty'):
        if(len(dq) == 0):
            print(1)
        else:
            print(0)
    if(cmd == 'front'):
        if(len(dq) == 0):
            print(-1)
            break
        print(dq[0])
    if(cmd == 'back'):
        if(len(dq) == 0):
            print(-1)
            break
        print(dq[-1])
