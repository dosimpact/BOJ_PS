from collections import deque


dq = deque([1, 2, 3, 4])
dq.append(10)
dq.popleft()
print(dq)
dq.rotate(1)
print(dq)
dq.rotate(-1)
print(dq)

dq.rotate(2)
print(dq)
dq.rotate(-2)
print(dq)
