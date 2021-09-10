# BOJ PS

# 언어환경셋팅

- env_python
- env_ts
- env_cpp
- env_node
- env_web

# 문제풀이 로그

```
- ./BOJ_난이도/**/*
- ./Programmers/**/*
- ./practice_kakao/**/*
```

# 개념 정리 로그

- ./BOJ_lecture
- ./DataStructure
- ./docs

```css
/* :root에 변수를 선언 */
/* 반드시 -- 으로 시작 */
:root {
  --bg: white;
  --color: #000;
}
/* 변수 사용은 var 키워드를 사용 */
body {
  background-color: var(--bg);
  color: var(--color);
}
/* 다크모드에서 변수를 변경가능  */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000;
    --color: white;
  }
}
/* //dark theme */
[data-theme="dark"] {
  --bg: #000;
  --color: white;
}
/* //light theme */
[data-theme="light"] {
  --bg: white;
  --color: #000;
}
```
