# 왜 branch들이 안보일까 merged 되었는데

# 코드 러너 익스텐션 설치!!

---

복습 문제:

- LST 문제: https://www.acmicpc.net/problem/11053
- 합문해 1,2 문제: https://www.acmicpc.net/problem/2225
- dp: [//https://www.acmicpc.net/problem/10942]
- 단순 오버플로우 / 문자열 : https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

* 그래프 - 싸이클 문제
  https://www.acmicpc.net/problem/9466

```
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr( (ord(s[i])-ord('A')+ n)%26+ord('A') )
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
```

복습 문제 : 유형(divmod for문)

- 1790 수 이어쓰기2
- 3101 토끼의 이동 https://www.acmicpc.net/problem/
- 124 나라의 숫자 https://programmers.co.kr/learn/courses/30/lessons/12899

```js
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]
```

```js
def change124(n):
    num = ['1','2','4']
    answer = ""
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
```

---

# 백준 알고리즘 !

- 환경 설치하기.
  [https://webnautes.tistory.com/1158](https://webnautes.tistory.com/1158)
