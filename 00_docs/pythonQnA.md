# https://www.acmicpc.net/problem/12813

```
a = int(input(), 2)
b = int(input(), 2)
m = 2**10**2

print(*(bin(c)[2:].zfill(10**2)
        for c in[a & b, a | b, a ^ b, m+~a, m+~b]), sep='\n')
```

```
# ÀÌ°Å¶û
print([c for c in [1, 2, 3]])

# ÀÌ°Å¶û
print(*(c for c in [1, 2, 3]))

```

```

import sys


def input(): return sys.stdin.readline().rstrip()


a = list(map(int, input()))
b = list(map(int, input()))
tmp = [0]*len(a)


def sol(func):
    for i in range(len(a)):
        tmp[i] = func(a[i], b[i]) % 2
    print(''.join(map(str, tmp)))


sol(lambda x, y: x & y)
sol(lambda x, y: x | y)
sol(lambda x, y: x ^ y)
sol(lambda x, y: ~x)
sol(lambda x, y: ~y)

```
