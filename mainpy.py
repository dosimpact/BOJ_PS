# 리스트 append sort reverse index insert remove pop count extend

a = [50, 20, 3, 4, 5]
a.append(6)
print(a)  # [50, 20, 3, 4, 5, 6]

a.extend([7, 8])
print(a)  # [50, 20, 3, 4, 5, 6, 7, 8]

a.sort()
print(a)  # [3, 4, 5, 6, 7, 8, 20, 50]

a.sort(reverse=True)
print(a)  # [50, 20, 8, 7, 6, 5, 4, 3]

a.reverse()
print(a)  # [3, 4, 5, 6, 7, 8, 20, 50]

idx = a.index(20)  # 현재 20의 위치는 6번째.
print(idx)  # 6

a.insert(idx, 21)  # 20위치가 하나 밀리고, 21이 들어감
print(a)  # [3, 4, 5, 6, 7, 8, 21, 20, 50]

a.remove(21)  # 21 찾아서 제거
print(a)  # [3, 4, 5, 6, 7, 8, 20, 50]

a.pop()
a.pop()
print(a)  # [3, 4, 5, 6, 7, 8]

print([3, 3, 3, 2, 2, 1].count(3))  # 3
