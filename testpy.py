# 이거랑
print([c for c in [1, 2, 3]])

# 이거랑
print(*(c for c in [1, 2, 3]))

a = int(input(), 2)
b = int(input(), 2)
m = 2**10**2

print(*(bin(c)[2:].zfill(10**2)
        for c in[a & b, a | b, a ^ b, m+~a, m+~b]), sep='\n')
