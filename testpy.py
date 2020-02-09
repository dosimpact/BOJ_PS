n = int(input())
b1 = [(int(m), i+1) for i, m in enumerate(input().split())]
i = 0

for b in range(n):
    d, ind = b1.pop(i)
    print(ind, end=' ')
    if b == n-1:
        break
    if d > 0:
        i = (i+d-1) % len(b1)
    else:
        i = (i+d) % len(b1)
