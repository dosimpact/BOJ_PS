import math

a = 0.19801980198020885

print(a)
print(round(a, 9))
if round(a, 9) != 0:
    # 가능성
    print(a)
    print(1/a)
    print(math.ceil(1/a))
else:
    print(-1)
