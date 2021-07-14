## BOJ Env Settings

- example : A+B 코드

- 플렛폼이 리눅스면 파일을 읽고 아니라면 문자열을 읽어서 배열 stdin을 만든다.
-

```js
const TC = `
5
1 1
2 3
3 4
9 8
5 2
`;
const stdin =
  process.platform === "linux"
    ? require("fs").readFileSync("/dev/stdin").toString().split("\n")
    : TC.trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = Number(input());
while (t--) {
  console.log(
    input()
      .split(" ")
      .map(Number)
      .reduce((a, c) => a + c)
  );
}
```
