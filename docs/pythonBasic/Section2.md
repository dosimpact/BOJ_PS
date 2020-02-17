# Section2. 시퀀스 데이터 자료 구조

# 리스트 만들기 (range 객체 사용하기.)

```python
a = [] # 혹은 a = list()
b = list(range(10)) # 0부터 9까지 range 객체 만들어 list로 변환
print(b)

c = list(range(1, 5)) # [1, 2, 3, 4]
print(c)

c = list(range(1, 11, 2)) # [1, 3, 5, 7, 9] # 1부터 10까지 2씩증가 | 11포함 안됨
print(c)

c = list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 이 역시 0은 미 포함.
print(c)

# for문으로 문자열 리스트 -> 정수 리스트 변환 및 합

nlist = [int(x) for x in ['10', '20', '30']]
print(sum(nlist))

```

## 람다식 | map ( 각원소를 2씩 곱할수있다. ) | filter (배열에서 짝수인경우만 퉤)

```python

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

```

# enumerate()

```python
var = ['a', 'b', 'c']

for i, val in enumerate(var):
print(i, val)
```

# 2차원 배열

```python
a = [[10, 20], [30, 40], [50, 60]]

for x, y in a:  # 리스트 자체를 받아서 사용
    print(x, y)

for i in a:  # 리스트를 원소를 2번꺼내 사용
    for j in i:
        print(j, end=' ')

for i in range(len(a)):  # 길이만큼 사용
    for j in range(len(a[i])):
        print(a[i][j])

for i, x in enumerate(a):
    for j, y in enumerate(x):
        print(a[i][j])


for i, x in enumerate(a):
    for j, y in enumerate(x):
        print(y)
```

# 반복문으로 2차원 | 배열 만들기

```python
a = ['x' for i in range(3)]
print(a) # ['x', 'x', 'x']

a = [[0, 0, 0] for i in range(3)]
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a = [[0 for i in range(3)] for i in range(3)]
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for문으로 리스트 완성하기

nlist = [int(x) for x in ['10', '20', '30']]
print(sum(nlist))

```

# 튜플 만들기 ( 튜플은 읽기 전용 리스트 )

```python
c = tuple(range(0, 10)) # range to tuple
print(c) # print (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(c)) # tuple to list
```

# 시퀀스 활용.

- 시퀀스 자료형이란: 리스트, 튜플, range, string, bytes, bytearray = > 슬라이싱 등등 가능!

## 시퀀스 존재성.

```python
a = [0, 1, 2, 'a', "hello", True, [0, 'dos', True], (0, 'impact', False)]

print(1 in a) # 참
print(10 in a) # 거짓
print('a' in a) # 참
print(True in a) # 참

print(1 not in a) # 거짓
print(10 not in a) # 참
print('a' not in a) # 거짓
print(True not in a) # 거짓

print('ll' in a[4]) # 참

print('dos' in a[6])  # 참
print('do' in a[6])  # 거짓
print('do' in a[6][1])  # 참

print('impact' in a[7])  # 참
print('act' in a[7])  # 거짓
print('act' in a[7][1])  # 참
```

# 시퀀스 with => len + 곱하기 del

```python
a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9, 10]
st = 'hello'
print(len(st)) # 5
print(a+b) # [1, 2, 3, 4, 5, 6]
print(a*2) # [1, 2, 3, 1, 2, 3]
print(a[-1]) # 3 (뒤에서 첫번째)

del a[1] # 1번째 인덱스 삭제
print(a) # [1, 3]
```

# 시퀀스 with => slice [][:]

```python
print(b[0:2]) # [4, 5]
print(b[0:]) # [4, 5, 6, 7, 8, 9, 10]
print(b[0:-1]) # [4, 5, 6, 7, 8, 9]
print(b[0:-1:2]) # 2씩 증가하면서 가져오기 [4, 6, 8]

print(b[::2]) # [4, 6, 8, 10] 짝수번 인덱스만 가져오기.

print(b[::-1]) # 뒤 집기 [10, 9, 8, 7, 6, 5, 4]

print(b[1::] + b[0:1:]) # 로테이션 [5, 6, 7, 8, 9, 10, 4]
```

# join 함수 : 리스트사이사이 특정 문자열을 넣고, 하나의 문자열로 만들어준다. ( splite와 반대대는 개념)

```
var = ['A', 'B', 'C']

print(''.join(var))  # ABC
print('|'.join(var))  # A|B|C
```
