s = [1, 2, 3]
print(s)

s.append(s.pop(0))
print(s)


s.insert(0, s.pop())
print(s)
