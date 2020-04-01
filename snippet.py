

ar = {1, 2, 3}
br = {2, 3, 4}
print(ar)
print(ar | br)


d = {}
print(d)
d[0] = ar
d[1] = br
d[2] = {4, 5, 6}
print(d)
print(d[0] & d[1])
print(len(d[0]))

print(*[1, 2, 3, 4])  # 1 2 3 4
