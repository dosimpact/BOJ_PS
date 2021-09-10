// 변수명 = 숫자
// print 변수명 , error 출력
// *동일 이름 여러개 출력 가능
// *블록이라는 개념, 가장 나중에 생성된 변수 출력
const res = new Array();
const scope = new Array(30).fill(0).map((e) => new Object());
function printCode(lastStr, dotCount) {
  // .의 갯수 이하부터 돌면서 변수를 출력하려함, 없으면 애러
  const key = lastStr.split(" ")[1];
  for (let i = dotCount; i >= 0; i--) {
    if (key in scope[i]) {
      res.push(`${key}=${scope[i][key]}`);
      return;
    }
  }
  res.push("error");
  return;
}

function solution(codes) {
  for (let code of codes) {
    // .. 이 갯수 찾기
    const lastDotIdx = String(code).lastIndexOf(".");
    const dotCount = lastDotIdx + 1;
    const lastStr = String(code).slice(dotCount);
    if (lastStr.includes("print")) {
      printCode(lastStr, dotCount);
    } else {
      // 변수를 해당 블록 레벨에 추가
      const [key, value] = lastStr.split("=");
      scope[dotCount] = {
        ...scope[dotCount],
        [key]: value,
      };
    }
  }
  return res;
}

// console.log(
//   solution([
//     "a=3",
//     "..a=4",
//     "..b=3",
//     "..print a",
//     ".......a=6",
//     ".......print a",
//     ".......print b",
//     "..print a",
//     "....a=7",
//     "....print a",
//     "print a",
//     "print b",
//     "a=4",
//     "print a",
//     "...print a",
//   ])
// );

console.log(
  solution([
    "x=3",
    "x=4",
    "z=5",
    "..x=99",
    "..y=98",
    "..z=97",
    ".print x",
    ".print y",
    ".print z",
    "...print x",
    "...print y",
    "...print z",
    ".......a=6",
    ".......print a",
    ".......print b",
  ])
);
