# Section3. 시퀀스 데이터 알고리즘

# sum,min,max,sorted | 합,최소,최대,정렬

```python
var = [1, 2, 3, 4, -1, 100]

print(sum(var))  # 109
print(min(var))  # 01
print(max(var))  # 100
print(sorted(var))  # [-1, 1, 2, 3, 4, 100]
print(sorted(var, reverse=True))  # [100, 4, 3, 2, 1, -1]

var = (1, 2, 3, 4, -1, 100)

print(sum(var))  # 109
print(min(var))  # 01
print(max(var))  # 100
print(sorted(var))  # [-1, 1, 2, 3, 4, 100]

var = "EABCD"
# print(sum(var))  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(min(var))  # A
print(max(var))  # E
print(sorted(var))  # ['A', 'B', 'C', 'D', 'E']
```

# 파이썬 정렬하기 | 커스텀 정렬

```python
# data.sort() 역시 정렬후, None반환 -> 원본이 훼손된다.

# sorted(리스트,reverse,key) 는 원본 훼손 없이 사용 가능


data = ['su', 'bed', 'app', 'king']

res = sorted(data)
print(res)  # ['bed', 'king', 'su']

res = sorted(data, reverse=True)
print(res)  # ['su', 'king', 'bed']

res = sorted(data, key=lambda x: len(x))  # 길이가 작은순
print(res)  # ['su', 'bed', 'app', 'king']

res = sorted(data, key=lambda x: (len(x), x))  # 길이가 작은순 + 사전순
print(res)  # ['su', 'app', 'bed', 'king']

res = sorted(data, key=lambda x: (len(x), x), reverse=True)  # 길이가 작은순 + 사전순
print(res)  # ['king', 'bed', 'app', 'su']
```

# 리스트 append sort reverse index insert remove pop count extend | push,pop | 정렬, 위치, 갯수,

```python
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
```

# 딕셔너리 사용(obj)

```python

x = {'base': 1, 'dos': 20}
print(x['base'])

# 피보나치 + dp for문 | dp 재귀

d = {}


def dp(n):
    if(n <= 1):
        return n
    if((n) in d):
        return d[(n)]
    d[n] = dp(n-1)+dp(n-2)
    return d[n]


var = int(input())
d[0] = 0
d[1] = 1
for i in range(2, var+1):
    d[i] = d[i-1] + d[i-2]
print(dp(var))


```

# python - 덱 ( 큐대신 댁을 쓰기. 큐는 시퀀서가 아니다.) | 로테이션도 추가되어 있음.

```python
from collections import deque

dq = deque([1, 2, 3, 4])

print(dq[0])  # front
print(dq[-1])  # back
print(len(dq))  # size

dq.append(5)  # push_back
dq.appendleft(6)  # push_front

print(dq.pop())  # pop_back
print(dq.popleft())  # pop_front

dq.rotate()
print(list(dq))
```

# set 함수 정리 (존재성 사용법은 동일)

```python
var = [5, 1, 1, 2, 2, 2, 3, 3, 3, 3]

print(set(var))  # 내부적으로 obj인듯 {1, 2, 3, 5}

var = list(set(var))
var.sort()
print(var)  # unique 중복제거 && 정렬 [1, 2, 3, 5]
```

# 우선순위 큐 사용하기. heappush,heappop,heapify

```python
import heapq

# 힙 만들기 push = logn && n개 원소 = n => 총 시간 복잡도 : nlogn
h = []  # 우선순위 큐로 사용될 리스트
heapq.heappush(h, (3, "Go to home"))  # 두번쨰 인자는 (우선순위,값)
heapq.heappush(h, (10, "Do not study"))
heapq.heappush(h, (1, "Enjoy!"))
heapq.heappush(h, (4, "Eat!"))
heapq.heappush(h, (7, "Pray!"))
print(h)


# 힙 꺼내기 nlogn
print(heapq.heappop(h))  # 우선순위 순서대로 나온다. 1 -> 3 -> 4 -> 7 -> 10
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))

# 힙 만들기 by 이미  만들어진 리스트 -> 힙 정렬 : O(n) 걸림
hlist = [(7, 'kdy'), (2, 'dos'), (4, 'hello')]

heapq.heapify(hlist)
print(heapq.heappop(hlist))
print(heapq.heappop(hlist))
print(heapq.heappop(hlist))

```

# 순열 조합 정리 permutations combinations import itertools

```python
import itertools

pool = ['A', 'B', 'C']

# 결과는 튜플로 반환된다. -> join을 통해 하나의 문자열로 뭉처줄 수 있다.

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(list(itertools.permutations(pool)))

#['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(list(map(''.join, itertools.permutations(pool))))  # 3개의 원소로 수열 만들기
#['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기

# [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.combinations(pool, 2)))
# ['ABC']
print(list(map(''.join, itertools.combinations(pool, 3))))  # 3개의 원소로 수열 만들기
#['AB', 'AC', 'BC']
print(list(map(''.join, itertools.combinations(pool, 2))))  # 2개의 원소로 수열 만들기
```

# python - bitset

```python

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
