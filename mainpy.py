
# 람다식 | map ( 각원소를 2씩 곱할수있다. ) | filter (배열에서 짝수인경우만 퉤)
# (x,y) => x+y
# lamda x,y: x+y


def g(x): return x**2


(a, b, c) = map(g, [1, 2, 3])  # 람다 없이 각 원소 2제곱
print(a, b, c)


(a, b, c) = map(lambda x: x*2, [1, 2, 3])  # 람다로, 각 원소 2곱
print(a, b, c)

res = list(map(lambda x: x*2, [1, 2, 3]))  # 람다로, 각 원소 2곱
print(res)

wannaEven = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(filter(lambda e: e % 2 == 0, wannaEven))  # filter오브젝트에서 list로 반환하기.
print(res)
