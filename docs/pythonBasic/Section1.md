# Section1. 변수 연산 입력 출력

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



```

# 아스키코드 (int) -> chr 변환 및 역 변환 ord

```python
data = 97

data = chr(data)
print(data) # a
print(type(data)) # <class 'str'>

data = ord(data)
print(data) # 97
print(type(data)) # <class 'int'>
```

# bool 과 논리

```python
if(True and False or not True):
    while(True):
        if(bool('False')):  # 모든 문자열은 참값!!!
            break
```

# 비트 연산자 및 진수 변환

```python
# 1. int 10진수를 통해 -> 비트 연산자 가능 ( 보기에는 10진수지만 내부적으로는 bit연산 잘 되고 있음)
# 2. int 10진수를 -> str 형태의 2진수,8진수,16진수 로 출력 가능
# 3. str형태를 자시 int 10진수로 변환 가능


# 1. int 10진수를 통해 -> 비트 연산자 가능 ( 보기에는 10진수지만 내부적으로는 bit연산 잘 되고 있음)

var = 1
print(var << 1)  # 2
print(var << 2)  # 4
print(var << 3)  # 8
print(7 | 5)  # 7

# 2. 십진수 int -> str : 이진수, 팔진수, 16진수 변환 및 출력


var = bin(7)
print(type(var))  # <class 'str'>
print(var)  # 0b111

var = hex(15)
print(type(var))  # <class 'str'>
print(var)  # 0xf

var = oct(8)
print(type(var))  # <class 'str'>
print(var)  # 0o10

# 3. str : 이진수, 팔진수, 16진수  -> int 십진수  변환 및 출력

var = '0b111'
print(int(var, 2))  # 7

var = '0xf'
print(int(var, 16))  # 15

var = '0o10'
print(int(var, 8))  # 8

# 4. 포멧을 가진 : 이진수, 팔진수, 16진수  -> int 십진수  변환 및 출력

print(0b101)  # 십진수로 5

print(0o10)  # 십진수로 8

print(0xF)  # 십진수로 15

# 예제 ) 출력 진수 포멧 정하기 ( 2진수,8진수,16진수  문자열을 -> 10진수로 출력)
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

print(a, end='')  # output 102030
print(b, end='')
print(c, end='\n')

print(a, end=' ')  # output 10 20 30
print(b, end=' ')
print(c, end='')


```

# python - 기본 입력은 이걸로 ~ 빠른 입력하기.

# def input(): return sys.stdin.readline().rstrip()

```python

# 한줄 한줄 읽기 | 보통 많이 사용하는듯 : rstrip()  # 해당 문자열의 공백 및 개행 제거
import sys

var = ' hi \n'
print(len(var))  # 5

var = var.rstrip()  # 해당 문자열의 공백 및 개행 제거
print(len(var))  # 3

var = var.strip()  #
print(len(var))  # 2
# 리스트에서 여러개 받는데 몇개인지 모를경우

a, *b = [1, 2, 3, 4, 5, 6]
print(a)  # 그냥 int 1
print(b)  # 리스트 형태 [2, 3, 4, 5, 6]


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
