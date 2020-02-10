# 기본문법 - 에디터 부터

---

## C/C++/STL 기초 to Python

## 변수 | 타입 | 기본연산 | 진수

```python

#  기본 연산자
print(7/3)  # 소수점 챙기는 나눗셈
print(7//3)  # 소수점 버리는 나눗셈
print(7 % 3)  # mod
print(2 ** 3)  # pow

# 몫 과 나머지
print(divmod(7, 3))  # 튜플로 (2,1) 반환.

# 형 출력 및 형 변환
print(type(3.3))  # float 형 출력
print(int(3.3))  # 소수점 버리기 | int형
print(int('10'))  # string to int
print(str(10)) # int to str

# 2,8,16 진수 포멧 및 출력

print(0b101)  # 십진수로 5

print(0o10)  # 십진수로 8

print(0xF)  # 십진수로 15

# 출력 진수 포멧 정하기
# https://www.acmicpc.net/problem/11816
a = input()
if(a[0] == '0'):
    if(a[0:2] == '0x'):
        print(int(a[2:], 16))
    else:
        print(int(a[1:], 8))

else:
    print(int(a))

```

# 나머지 연산의 개념 => 양수는 직관적인데, 음수는 -1이 가르키는 배열이 마지막 배열임을 안다면 별거없다.

```python
"""
0 1 2 3 4 <- 배열 길이 : 5

0 1 2 3 4
5 6 7 8 ...

-5 -4 -3 -2 -1
.. -9 -8 -7 -6

"""

var = [0, 1, 2, 3, 4]

print(len(var)) # 길이 5

print(0 % len(var)) # 0 ~ 4
print(1 % len(var))
print(2 % len(var))
print(3 % len(var))
print(4 % len(var))

print(5 % len(var)) # 0 ~ 4
print(6 % len(var))
print(7 % len(var))
print(8 % len(var))
print(9 % len(var))

print(-1 % len(var)) # 4 ~ 0
print(-2 % len(var))
print(-3 % len(var))
print(-4 % len(var))
print(-5 % len(var))

print(-6 % len(var)) # 4 ~ 0
print(-7 % len(var))
print(-8 % len(var))
print(-9 % len(var))
print(-10 % len(var))
```

## 변수 (선언)

```python
# variable & type

a, b, c = 10, '20', 30

print(a, b, c)
print(type(a), type(b), type(c))

# Swap

a, c = c, a
print(a, b, c)

# variable => None | del ( 즉 , None 과 not defined는 다르다.!!)

var1 = 10
del var1
# print(var1) # NameError: name 'var1' is not defined
var1 = None
print(var1)  # None

```

## 변수 (입력,출력)

```python
# input

var1 = input()  # input : 10 | str 형으로 입력됨
print(type(var1))

var1 = int(input())  # input : 10 | int로 형 변환
print(type(var1))


# input 한줄을 받아서, 공백으로 구분하기 하지만 str로 들어감

u, v = input().split()
print(u, v)
print(type(u), type(v))

# input 바로 int형으로 받는 방법.

u, v = map(int, input().split())
print(u, v)
print(type(u), type(v))

# print 마다  \n 을 넣기

a, b, c = map(int, input().split(','))  # input 10,20,30
print(a, b, c, sep='\n')  # output 10\n20\n30

# print 마다  \n 을 넣기

a, b, c = map(int, input().split(','))  # input 10,20,30
print(a, b, c, sep='\n')  # output 10\n20\n30

print(a, end='')  # output 102030
print(b, end='')
print(c, end='\n')

print(a, end=' ')  # output 10 20 30
print(b, end=' ')
print(c, end='')


```

# python - 기본 입력은 이걸로 ~

```python

# 한줄 한줄 읽기 | 보통 많이 사용하는듯 : rstrip()  # 해당 문자열의 공백 및 개행 제거
import sys

var = ' hi \n'
print(len(var))  # 5
var = var.rstrip()  # 해당 문자열의 공백 및 개행 제거
print(len(var))  # 3

# 리스트에서 여러개 받는데 몇개인지 모를경우

a, *b = [1, 2, 3, 4, 5, 6]
print(a)
print(b)

# print 안에 if문 사용

print('하하하' if False else '노노노')  # 노노노

# [] 안에 if문 사용

var = ['하하하' if True else 'nonono']
print(var)  # ['하하하']

# 실전 한줄씩 읽기
# https://www.acmicpc.net/problem/10866
from collections import deque
import sys


def input(): return sys.stdin.readline().rstrip()


dq = deque()
t = int(input())

for _ in range(t):
    a, *b = input().split()
    if(a == 'push_front'):
        dq.appendleft(b[0])
    elif(a == 'push_back'):
        dq.append(b[0])
    elif(a == 'pop_front'):
        print(dq.popleft() if len(dq) != 0 else -1)
    elif(a == 'pop_back'):
        print(dq.pop() if len(dq) != 0 else -1)
    elif(a == 'size'):
        print(len(dq))
    elif(a == 'empty'):
        print(0 if len(dq) != 0 else 1)
    elif(a == 'front'):
        print(dq[0] if len(dq) != 0 else -1)
    elif(a == 'back'):
        print(dq[-1] if len(dq) != 0 else -1)


```

# python - 입력 정리, EOF 까지 | 한줄 그냥 | spilt 이용해서

```python
# 문자열 한줄을 그냥 받기
a = input()
print(a)

# 공백을 제외한 알맹쓰만 받기 -> 리스트로 반환됨
a = input().split()
print(a)

# EOF(ctrl+Z) 까지 한줄 한줄 입력받기 (공백 포함 싹다 포함)

# https://www.acmicpc.net/problem/11718
import sys

for line in sys.stdin:
    a = line
    print(a, end='')  # line자체가 enter를 포함학 있다.

# EOF(ctrl+Z) 한번에 입력받기 (공백 포함 싹다 포함)

# https://www.acmicpc.net/problem/11718
import sys
v = sys.stdin.read()
print(v, end='')

# EOF(ctrl+Z) 까지 한줄 한줄 입력받기 (공백 없이 알맹이 문자열만)

import sys

for line in sys.stdin:
    a = line.split()
    print(a)

# EOF(ctrl+Z) 까지 정수 a,b  입력받기

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

# EOF 까지 한번에 읽어서, 뛰어쓰기는 제거하고 ,로 나눠서 리스트를 반환후 더한값을 출력하기
# https://www.acmicpc.net/problem/10823
import sys

nlist = [int(x) for x in sys.stdin.read().replace('\n', '').split(',')]
print(sum(nlist))

#  공백 포함 문자열 하나하나 분리하기

a = input()
print(list(a))

#  공백 제거 후 문자열 하나하나 분리하기

a = input().split()
for e in a:
    print(list(e))

#  1234 숫자 입력시 , 1,2,3,4 로 하나씩 끊어 받기 ( 공백 처리 불가능  )

a = list(input())
res = list(map(int, a))

print(res)

#  1234 숫자 입력시 , 1,2,3,4 로 하나씩 끊어 받기 ( 공백 처리 가능 )
ans = []
a = input().split()
for e in a:
    res = list(map(int, e))
    ans.extend(res)

print(ans)



# 뛰어쓰기 처리하기 -> replace('\n','')

import sys

var = sys.stdin.read()
var = (var.replace('\n', '').split(','))
print(sum(list(map(int, var))))






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

# bool 과 논리

```python
if(True and False or not True):
    while(True):
        if(bool('False')):  # 모든 문자열은 참값!!!
            break
```

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

# sum,min,max,sorted

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

# 리스트 append sort reverse index insert remove pop count extend

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

# python - 덱 ( 큐대신 댁을 쓰기. 큐는 시퀀서가 아니다.)

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

//2.2 출력시 소수점 처리하기
#include<iomanip>
setprecision(5)
fixed
eg)
double f = 3.1415926535;
cout<<setprecision(5)<<f; //앞에서 5번째까지 출력(반올림적용)

cout<<fixed<<setprecision(5)<<f; //소수점 자리부터 5번째 가지 출력(반올림 적용)

//3.6 list 이중연결 리스트 : insert와 erase는 O(1)이 걸림
#include<list>

list<int> l ={2,1,-5};
l.sort(); // 기본 : 오름차순
l.sort(greater<int>());//내림차순
l.sort([](int& u,int& v){return abs(u)<abs(v);}); //커스텀 정렬
l.reverse

//순차 컨테이너 : vector list deque
//연관 컨테이너 : set map

//3.8 set 삽입 삭제 탐색에 log(n) 걸림
#include<set>

set<int> s1;
set<int> s2 = {1,2,3,4} // 자동 오름차 정렬 저장 및 중복 제거됨
set<int,greater<int>> s3 // 자동 내림차 정렬 하기

eg)
s1.insert(4); // 대입
pair<set<int>::iterator, bool > result = s2.insert(4); //결과 반환(넣은 위치,성공 여부)

    s1.erase(s.begin()); //삭제
    s1[] X //set은 순서 가 아니야
    auto it = s.erase(s.begin()+1);//{1,2,3,4} -> {1,3,4}
    it = s.erase(it) //{1,3,4} -> {1,4}

eg)
set은 for 나 foreach로 순회가 가능하다. lgN

eg)
s = {1,3,5,7}
auto it = s.find(1); //{1,3,5,7} 첫번재 원소를 가르킴
//없으면 s.end()를 반환함

    s.count(7) // 원소 7이 몇개? 1개

//3.8.2 multiset: 같은 원소 여러개를 저장 가능하다.

정리)
<T>.count의 의미
map,unordered_map,set 에서는 0또는 1 (생성하지 않고 존재 유무 )
multiset 에서는 0또는 N( 존재 및 갯수)

//컨테이너 어댑터 : stack,queu,우선큐,bitset : 앞의 자료구조로 만듬.

//3.12 priority_queue - #include<queue>에 같이 동봉됨.

#include<queue>

    priority_queue<int> pq;

    pq.push()
    pq.pop()
    pq.top() //  우선 큐는 특이하게 front 가 아닌 top 이다. tree형 stack을 연상하나봄.
    pq.empty() pq.size()

eg) 우선큐는 기본적으로 오름차 순으로 정렬된다. 그럼 내림차 우선 큐는 어떻게 만드나? 1. priority_queue<int,vector<int>,greater<int>> q3; 2. 입력시 pq.push(-x); 출력시 -pq.top() // a<b 는 -a > -b 이므로 -를 붙여 반대순서로 넣고/ 출력시 -붙여 원상복귀

//3.13 bitset

//vector<bool> 형태 , 1bit만 사용한다.

bitset<10> b2(88) //10자리 2진수를 만드는데, 십진수 88을 넣을꺼임
bitset<10> b2("10010")//10자리 2진수를 만드는데, 2진수 10010을 넣을꺼임
bitset<n> b2 // 애러

    bitset<100000>a;
    bitset<100000>b;

    cin >> a >> b;

    cout << (a & b) << '\n'; //AND
    cout << (a | b) << '\n'; //OR
    cout << (a ^ b) << '\n';	//XOR
    cout << ~(a) << '\n';	//NOT
    cout << ~(b);		//NOT

eg)참조

b2[i]
b2.test(i)

b.flip() b.flip(1) // 0 => 1, 1 => 0
b.set() b.set(1) // 0,1 => 1로
b.reset() b.reset(1) //0,1 => 0으로

b.all() //모두 1?
b.any() //적어도 한개는 1?
b.none() //모두 0?
b.count()//1이 몇개인가?

//삽입 삭제 시간 --> 백터는 N , set은 lgN, 리스트는 1
//count의 의미 set에서는 존재성 / multiset 에서는 갯수 / STL의 count도 갯수, map,unordered_map에서 존재성

Sec5. STL - Algorithm

//#5.5 회전하기
rotate(begin,mid,end);
[mid,end)를 앞으로, [begin,mid)를 뒤로 위치 바꾸기.
rotate(begin,begin+1,end); //오른쪽으로 한칸씩 이동하기
rotate(begin,end-1,end); //왼쪽으로 한칸씩 이동하기

---//#5.7 unique 구간에서 연속된 값을 제거하고 하나만 만들고 다시 넣는다.
정렬 -> 유니크 -> erase
vector<int> v;
v.sort(); // 1.정렬
auto it = v.unique(v.begin(),v.end()); //2. 유니크
erase(it,v.end()); // 3. 잔존 지우기

//#5.9 이진 탐색, 보통 커스터 직접 만드는 경우가 흔한데,
binary_search(begin,end,value); //true or false
binary_search(begin,end,value,cmp); // true or false

---

//#5.12 순열

next_permutation(v.begin(),v.end()); //다음 순열
prev_permutation(v.begin(),v.end()); //이전 순열
